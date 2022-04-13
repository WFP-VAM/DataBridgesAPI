# Method to call DataBridges API
import backoff
import httpx


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
        'url': 'vam-data-bridges/1.2.0/Commodities/List',
        'method': 'GET'
    },
    'monthly_prices': {
        'url': 'vam-data-bridges/1.2.0/MarketPrices/PriceMonthly',
        'method': 'GET'
    },
    'weekly_prices': {
        'url': 'vam-data-bridges/1.2.0/MarketPrices/PriceWeekly',
        'method': 'GET'
    },
    'market_list': {
        'url': 'vam-data-bridges/1.2.0/Markets/List',
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

    def get_weekly_prices(self, iso3):
        page = 1
        all_data = []
        data_mp = None
        while data_mp is None or len(data_mp) > 0:
            print(f'fetching price data page {page}')
            data_mp = self._invoke('weekly_prices', {'CountryCode': iso3, 'page': page})['items']
            all_data.extend(data_mp)
            page = page + 1
        return all_data

    def get_market_list(self, iso3):
        page = 1
        all_data = []
        data_mp = None
        while data_mp is None or len(data_mp) > 0:
            print(f'fetching market list page {page}')
            data_mp = self._invoke('market_list', {'CountryCode': iso3, 'page': page})['items']
            all_data.extend(data_mp)
            page = page + 1
        return all_data


MY_KEY = ''
MY_SECRET = ''

api = WfpApi(api_key=MY_KEY, api_secret=MY_SECRET)
commodityData = api.get_commodity_list('YEM')
#priceData = api.get_monthly_prices('YEM')
weeklyPriceData = api.get_weekly_prices('YEM')
marketsData = api.get_market_list('YEM')

#import pandas as pd
#import json

import csv


output_file = 'result_meetup.csv'
length_data = len(commodityData) - 1
data_to_file = open(output_file, 'w')
csv_writer = csv.writer(data_to_file)
header = commodityData[0].keys()
csv_writer.writerow(header)
for row in commodityData:
    meetup = row.values()
    csv_writer.writerow([meetup])
data_to_file.close()

commodityData.to_csv(r'Commodities.csv')


def flattenjson(b, delim):
    val = {}
    for i in b.keys():
        if isinstance(b[i], dict):
            get = flattenjson(b[i], delim)
            for j in get.keys():
                val[i + delim + j] = get[j]
        else:
            val[i] = b[i]

    return val




input = map(lambda x: flattenjson( x, "__" ), input)



commodityData.to_csv(r'commodityData.csv', index = None)

#df1 = pd.read_json(marketsData)
#df1.to_csv(r'marketsData.csv', index = None)
#df1 = pd.read_json(weeklyPriceData)
#df1.to_csv(r'weeklyPriceData.csv', index = None)

pass
token() {
curl -k -d "grant_type=client_credentials&scope=$1" -H "Authorization: Basic
MY_KEY:MY_SECRET" https://api.wfp.org/token
}