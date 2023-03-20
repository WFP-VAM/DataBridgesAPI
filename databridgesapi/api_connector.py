import backoff
import httpx
import datetime
from loguru import logger
from typing import Optional, Any, List, Dict

from exceptions import *


class DataBridgesAPI:
    BASE_URL = "https://api.wfp.org"

    def __init__(self, api_key: str, api_secret: str):
        """
        Args:
            api_key: API key credential to make API requests
            api_secret: API secrets credential to make API requests
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.tokens_by_scopes = {}
        self.__api_endpoint = {
            "commodities_list": {
                "url": "vam-data-bridges/1.3.1/Commodities/List",
                "method": "GET",
            },
            "monthly_prices": {
                "url": "vam-data-bridges/1.3.1/MarketPrices/PriceMonthly",
                "method": "GET",
            },
            "weekly_prices": {
                "url": "vam-data-bridges/1.3.1/MarketPrices/PriceWeekly",
                "method": "GET",
            },
            "monthly_alps": {
                "url": "vam-data-bridges/1.3.1/MarketPrices/Alps",
                "method": "GET",
            },
            "market_list": {
                "url": "vam-data-bridges/1.3.1/Markets/List",
                "method": "GET",
            },
            "currency_exchange": {
                "url": "vam-data-bridges/1.3.1/Currency/UsdIndirectQuotation",
                "method": "GET",
            },
            "food_inflation": {
                "url": "vam-data-bridges/1.3.1/EconomicData/Food%20Inflation",
                "method": "GET",
            },
            "headline_inflation": {
                "url": "vam-data-bridges/1.3.1/EconomicData/Inflation%20Rate",
                "method": "GET",
            },
        }

    def show_supported_endpoint(self):
        return self.__api_endpoint.keys()

    def _refresh_token(self, scopes: Optional[str] = None):
        """
        Refreshes token to make API requests
        Args:
            scopes: API scopes. The default is None

        """
        resp = httpx.post(
            f"{self.BASE_URL}/token",
            data={"grant_type": "client_credentials", "scope": " ".join(scopes)},
            auth=(self.api_key, self.api_secret),
        )
        resp.raise_for_status()
        resp_data = resp.json()
        received_scopes = set(resp_data["scope"].split(" "))
        if not set(scopes).issubset(received_scopes):
            raise TokenScopeError(f"Could not acquire requested scopes: {scopes}")
        self.tokens_by_scopes[scopes] = resp_data["access_token"]

    @backoff.on_exception(
        backoff.expo, (ApiServerError, ApiNotAuthorizedError), max_tries=5
    )
    def _invoke(
        self,
        endpoint_name: str,
        params: Optional[Any] = None,
        body: Optional[Any] = None,
    ):
        """
        Makes the API calls
        Args:
            endpoint_name: endpoint identifier.
            params: parameters to be sent to the API. Parameters are options that influence the API response. Default is None.
            body: request body to be sent to the API. Default is None.

        Returns:
            The API response ad json

        """
        if endpoint_name not in self.__api_endpoint:
            raise ValueError("Invalid endpoint invoked. Check the system configuration")

        endpoint = self.__api_endpoint.get(endpoint_name)
        if params is None:
            params = {}
        scopes = endpoint.get("scopes", tuple())
        token = self.tokens_by_scopes.get(scopes, "")
        if token == "":
            self._refresh_token(scopes)
            token = self.tokens_by_scopes.get(scopes, "")

        with httpx.Client(base_url=self.BASE_URL) as client:
            headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
            resp = client.request(
                endpoint["method"],
                endpoint["url"],
                params=params,
                json=body,
                timeout=None,
                headers=headers,
            )

            if resp.status_code == httpx.codes.UNAUTHORIZED:
                self._refresh_token(scopes)
                logger.info("unauthorized. Retrying...")
                raise ApiNotAuthorizedError()
            elif resp.status_code >= httpx.codes.INTERNAL_SERVER_ERROR:
                logger.info("Internal server error. Retrying...")
                raise ApiServerError()
            elif resp.status_code == httpx.codes.NOT_FOUND:
                raise NotFoundError()
            elif (
                httpx.codes.BAD_REQUEST
                <= resp.status_code
                < httpx.codes.INTERNAL_SERVER_ERROR
            ):
                logger.info("Http client error! Not retrying (as it would be useless)")
                raise HTTPError(f"HTTP Client error ({resp.status_code})")
            else:
                return resp.json()

    def get_commodity_list(self, iso3: str) -> List[Dict[str, str]]:
        page = 1
        all_data = []
        data_cl = None
        while data_cl is None or len(data_cl) > 0:
            logger.trace(f"fetching page {page}")
            data_cl = self._invoke(
                "commodities_list", {"CountryCode": iso3, "page": page}
            )["items"]
            all_data.extend(data_cl)
            page = page + 1
        return all_data

    def get_monthly_prices(self, iso3: str):
        """

        Args:
            iso3: The code to identify the country. Must be a ISO-3166 Alpha 3 code.

        Returns:
            all_data: list of jsons containing the fetched data
        """
        page = 1
        all_data = []
        data = None
        while data is None or len(data) > 0:
            logger.trace(f"fetching price data page {page}")
            data = self._invoke("monthly_prices", {"CountryCode": iso3, "page": page})[
                "items"
            ]
            all_data.extend(data)
            page = page + 1
        return all_data

    def get_weekly_prices(self, iso3):
        page = 1
        all_data = []
        data = None
        while data is None or len(data) > 0:
            logger.info(f"fetching price data page {page}")
            data = self._invoke("weekly_prices", {"CountryCode": iso3, "page": page})[
                "items"
            ]
            all_data.extend(data)
            page = page + 1
        return all_data

    def get_market_list(self, iso3: str):
        page = 1
        all_data = []
        data = None
        while data is None or len(data) > 0:
            logger.info(f"fetching market list page {page}")
            data = self._invoke("market_list", {"CountryCode": iso3, "page": page})[
                "items"
            ]
            all_data.extend(data)
            page = page + 1
        return all_data

    def get_monthly_alps(
        self, iso3: str, start_date: datetime.date
    ) -> List[Dict[str, str]]:
        """

        Args:
            iso3: The code to identify the country. Must be a ISO-3166 Alpha 3 code.
            start_date: Starting date for the range in which data was collected.

        Returns:
            all_data: list of jsons containing the fetched data
        """
        page = 1
        all_data = []
        data_mp = None
        while data_mp is None or len(data_mp) > 0:
            logger.trace(f"fetching price data page {page}")
            data_mp = self._invoke(
                "monthly_alps",
                {"CountryCode": iso3, "startDate": start_date, "page": page},
            )["items"]
            all_data.extend(data_mp)
            page = page + 1
        return all_data

    def get_economic_indicator(
        self,
        economic_indicator: str,
        iso3: str,
        start_date: Optional[datetime.date] = None,
        end_date: Optional[datetime.date] = None,
    ) -> List[Dict[str, str]]:
        """
        Fetch data for the supported economic indicators, check the supported ones using the 'show_supported_endpoint' method.
        Args:
            economic_indicator: name of the economic indicator data should be fetched.
            iso3: The code to identify the country. Must be a ISO-3166 Alpha 3 code.
            start_date: Starting date for the range in which data was collected. Optional.
            end_date: Ending date for the range in which data was collected. Optional.

        Returns:
            all_data: list of jsons containing the fetched data
        """
        page = 1
        all_data = []
        data = None
        while data is None or len(data) > 0:
            logger.trace(f"Fetching {economic_indicator} data page {page}")
            data = self._invoke(
                f"{economic_indicator}",
                {
                    "iso3": iso3,
                    "startDate": start_date,
                    "endDate": end_date,
                    "page": page,
                },
            )["items"]
            all_data.extend(data)
            page = page + 1
        return all_data
