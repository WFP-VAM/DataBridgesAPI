# Method to call DataBridges API
import backoff
import httpx
import pandas
from datetime import date
import dateutil
from dateutil.relativedelta import relativedelta
import numpy as np


class HTTPError(Exception):
    pass


class ApiServerError(Exception):
    pass


class TokenScopeError(Exception):
    pass


class ApiNotAuthorizedError(Exception):
    pass


class NotFoundError(Exception):
    pass


API_ENDPOINTS = {
    'commodities_list': {
        'url': 'vam-data-bridges/1.1.0/Commodities/List',
        'method': 'GET'
    },
    'monthly_prices': {
        'url': 'vam-data-bridges/1.1.0/MarketPrices/PriceMonthly',
        'method': 'GET'
    },
    'monthly_alps': {
        'url': 'vam-data-bridges/1.1.0/MarketPrices/Alps',
        'method': 'GET'
    }
}


class WfpApi:
    BASE_URL = 'https://api.wfp.org'

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.tokens_by_scopes = {}

    def _refresh_token(self, scopes):
        resp = httpx.post(f'{self.BASE_URL}/token',
                          data={'grant_type': 'client_credentials', 'scope': ' '.join(scopes)},
                          auth=(self.api_key, self.api_secret))
        resp.raise_for_status()
        resp_data = resp.json()
        received_scopes = set(resp_data['scope'].split(' '))
        if not set(scopes).issubset(received_scopes):
            raise TokenScopeError(f'Could not acquire requested scopes: {scopes}')
        self.tokens_by_scopes[scopes] = resp_data['access_token']

    @backoff.on_exception(backoff.expo, (ApiServerError, ApiNotAuthorizedError), max_tries=5)
    def _invoke(self, endpoint_name, params=None, body=None):
        if endpoint_name not in API_ENDPOINTS:
            raise ValueError('Invalid endpoint invoked. Check the system configuration')

        endpoint = API_ENDPOINTS.get(endpoint_name)
        if params is None:
            params = {}
        scopes = endpoint.get('scopes', tuple())
        token = self.tokens_by_scopes.get(scopes, '')
        if token == '':
            self._refresh_token(scopes)
            token = self.tokens_by_scopes.get(scopes, '')

        with httpx.Client(base_url=self.BASE_URL) as client:
            headers = {'Accept': 'application/json', 'Authorization': f'Bearer {token}'}
            resp = client.request(endpoint['method'], endpoint['url'], params=params, json=body, timeout=None,
                                  headers=headers)

            if resp.status_code == httpx.codes.UNAUTHORIZED:
                self._refresh_token(scopes)
                print('unauthorized. Retrying...')
                raise ApiNotAuthorizedError()
            if resp.status_code >= httpx.codes.INTERNAL_SERVER_ERROR:
                print('Internal server error. Retrying...')
                raise ApiServerError()
            if resp.status_code == httpx.codes.NOT_FOUND:
                raise NotFoundError()
            if httpx.codes.BAD_REQUEST <= resp.status_code < httpx.codes.INTERNAL_SERVER_ERROR:
                print('Http client error! Not retrying (as it would be useless)')
                raise HTTPError(f'HTTP Client error ({resp.status_code})')

        return resp.json()

    def get_commodity_list(self, iso3):
        page = 1
        all_data = []
        data_cl = None
        while data_cl is None or len(data_cl) > 0:
            print(f'fetching page {page}')
            data_cl = self._invoke('commodities_list', {'CountryCode': iso3, 'page': page})['items']
            all_data.extend(data_cl)
            page = page + 1
        return all_data

    def get_monthly_prices(self, iso3):
        page = 1
        all_data = []
        data_mp = None
        while data_mp is None or len(data_mp) > 0:
            print(f'fetching price data page {page}')
            data_mp = self._invoke('monthly_prices', {'CountryCode': iso3, 'page': page})['items']
            all_data.extend(data_mp)
            page = page + 1
        return all_data

    def get_monthly_alps(self, iso3, startdate):
        page = 1
        all_data = []
        data_mp = None
        while data_mp is None or len(data_mp) > 0:
            print(f'fetching price data page {page}')
            data_mp = self._invoke('monthly_alps', {'CountryCode': iso3, 'startDate': startdate, 'page': page})['items']
            all_data.extend(data_mp)
            page = page + 1
        return all_data


MY_KEY = ''
MY_SECRET = ''

api = WfpApi(api_key=MY_KEY, api_secret=MY_SECRET)
commodities = api.get_commodity_list('GNB')

today = date.today()
delta = dateutil.relativedelta.relativedelta(months=6)
six_months_ago = today - delta

alpsData = api.get_monthly_alps('GNB', six_months_ago)

commodities = pandas.json_normalize(commodities)
alpsData = pandas.json_normalize(alpsData)
foodCommodities = commodities[commodities.categoryId < 8][['categoryId', 'id', 'name']]
subsetAlpsData = alpsData.set_index('commodityID').join(foodCommodities.set_index('id'), how='inner')
priceData = pandas.df(alpsData)

conditions = [
    subsetAlpsData['categoryId'] == 1,
    subsetAlpsData['categoryId'] == 2,
    subsetAlpsData['categoryId'] == 3,
    subsetAlpsData['categoryId'] == 4,
    subsetAlpsData['categoryId'] == 5,
    subsetAlpsData['categoryId'] == 6,
    subsetAlpsData['categoryId'] == 7,
]

outputs = [
    2, 4, 4, 1, 3, 0.5, 0.5
]

res = pandas.DataFrame(np.select(conditions, outputs, 0))


# pass
