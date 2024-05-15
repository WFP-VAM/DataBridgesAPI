import time
import data_bridges_client
from data_bridges_client.rest import ApiException
from pprint import pprint
from data_bridges_client.token import WfpApiToken
import yaml
import os
from datetime import timedelta
from datetime import date
import pandas as pd

class DataBridgesShapes:
    def __init__(self, yaml_config_path):
        self.configuration = self.setup_configuration_and_authentication(yaml_config_path)

    def __repr__(self):
        return f"DataBridgesShapes(yamlpath='{self.configuration.host}')"

    def __str__(self):
        return f"Brought you by... SHAPES"

    def setup_configuration_and_authentication(self, yaml_config_path):
        """Loads configuration from a YAML file and sets up authentication."""

        with open(yaml_config_path, "r") as yamlfile:
            databridges_config = yaml.load(yamlfile, Loader=yaml.FullLoader)

        key = databridges_config['KEY']
        secret = databridges_config['SECRET']
        scopes = databridges_config['SCOPES']
        version = databridges_config['VERSION']
        uri = "https://api.wfp.org/vam-data-bridges/"
        host = str(uri + version)
        print(host)

        token = WfpApiToken(api_key=key, api_secret=secret)
        configuration = data_bridges_client.Configuration(
            host=host,
            access_token=token.refresh(scopes=scopes)
        )
        return configuration

    def get_household_survey(self, survey_id, access_type, page_size=200):
        """Retrieves survey data using the specified configuration and access type.
        
        Args:
            survey_id (str): The ID of the survey to retrieve.
            access_type (str): The type of access to use for retrieving the survey data. Can be one of '', 'full', 'draft', 'official', or 'public'.
            page_size (int, optional): The number of items to retrieve per page. Defaults to 200.
        
        Returns:
            pandas.DataFrame: A DataFrame containing the retrieved survey data.
        """

        responses = []
        page_size = page_size
        total_items = 1
        max_item = 0
        page = 0

        while total_items > max_item:
            page += 1
            with data_bridges_client.ApiClient(self.configuration) as api_client:
                api_instance = data_bridges_client.IncubationApi(api_client)
                env = 'prod'

                try:
                    # Select appropriate API call based on access_type
                    api_survey = {
                        '': api_instance.household_public_base_data_get,
                        'full': api_instance.household_full_data_get,
                        'draft': api_instance.household_draft_internal_base_data_get,
                        'official': api_instance.household_official_use_base_data_get,
                        'public': api_instance.household_public_base_data_get
                    }.get(access_type)(survey_id=survey_id, page=page, env=env)
                    print(f"Fetching page {page}")
                    print(f"Items: {len(api_survey.items)}")
                    print("\n ---- \n")
                    responses.extend(
                        [item for item in api_survey.items]
                    )
                    total_items = api_survey.total_items
                    max_item = len(api_survey.items) + max_item
                    time.sleep(1)

                except ApiException as e:
                    print(f"Exception when calling Household data-> {access_type}{e}\n")
                    exit()

        df = pd.DataFrame(responses)
        return df

    def get_prices(self, country_iso3, survey_date, page_size=1000):
        """
        Fetches market price data for a given country and survey date.

        Args:
            country_iso3 (str): The ISO 3-letter country code.
            survey_date (str): The survey date in ISO format (e.g. '2022-01-01'). If an empty string is provided, the function will fetch data starting from January 1, 1990.
            page_size (int, optional): The number of items to fetch per page. Defaults to 1000.

        Returns:
            pandas.DataFrame: A DataFrame containing the fetched market price data.
        """

        if survey_date != '':
            start_date = date.fromisoformat(survey_date) - timedelta(days=365)
        else:
            start_date = date.fromisocalendar(1990, 1, 1)
        responses = []
        page_size = page_size
        total_items = 20
        max_item = 0
        page = 0
        while total_items > max_item:
            page = page + 1  # int | page number for paged results (optional) (default to 1)
            with data_bridges_client.ApiClient(self.configuration) as api_client:
                # Create an instance of the API class
                api_instance = data_bridges_client.MarketPricesApi(api_client)
                env = 'prod'  # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

                try:
                    # Provides the list of categories.
                    api_prices = api_instance.market_prices_price_monthly_get(
                        country_code=country_iso3,
                        format='JSON',
                        page=page,
                        env=env,
                        start_date=start_date)
                    responses.extend(
                        [item.to_dict() for item in api_prices.items]
                    )
                    total_items = api_prices.total_items
                    print("Fetching page %s" % page)
                    max_item = page * page_size
                    time.sleep(1)
                except ApiException as e:
                    print("Exception when calling Market price data->market_prices_price_monthly_get: %s\n" % e)
                    exit()
        df = pd.DataFrame(responses)
        return df

    def get_exchangerates(self, country_iso3, page_size=1000):
        """
        Retrieves exchange rates for a given country ISO3 code from the Data Bridges API.

        Args:
            country_iso3 (str): The ISO3 country code for which to retrieve exchange rates.
            page_size (int, optional): The number of items to retrieve per page. Defaults to 1000.

        Returns:
            pandas.DataFrame: A DataFrame containing the exchange rate data.
        """

        responses = []

        # Enter a context with an instance of the API client
        page_size = page_size
        total_items = 20
        max_item = 0
        page = 0
        while total_items > max_item:
            page = page + 1  # int | page number for paged results (optional) (default to 1)
            with data_bridges_client.ApiClient(self.configuration) as api_client:
                # Create an instance of the API class
                api_instance = data_bridges_client.CurrencyApi(api_client)
                env = 'prod'  # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

                try:
                    # Provides the list of categories.
                    api_exchange_rates = api_instance.currency_usd_indirect_quotation_get(
                        country_iso3=country_iso3,
                        format='JSON',
                        page=page,
                        env=env)
                    responses.extend(
                        [item.to_dict() for item in api_exchange_rates.items]
                    )
                    total_items = api_exchange_rates.total_items
                    print("Fetching page %s" % page)
                    max_item = page * page_size
                    time.sleep(1)
                except ApiException as e:
                    print("Exception when calling Exchange rates data->household_full_data_get: %s\n" % e)
                    exit()
        df = pd.DataFrame(responses)
        return df

    def get_ipc_equivalent(self, country_iso3: str, year: int, page_size=1000):
        """
        Retrieves food security data for a given country ISO3 code from the Data Bridges API.
        """
        responses = []
        page_size = page_size
        total_items = 20
        max_item = 0
        page = 0
        while total_items > max_item:
            page = page + 1  # int | page number for paged results (optional) (default to 1)
            with data_bridges_client.ApiClient(self.configuration) as api_client:
                # Create an instance of the API class
                api_instance = data_bridges_client.FoodSecurityApi(api_client)
                env = 'prod'  # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

                try:
                    # Provides the list of categories.
                    api_food_security = api_instance.food_security_list_get(
                        country_iso3=country_iso3,
                        year = year,
                        page=page,
                        env=env,
                        )
                    responses.extend(
                        [item.to_dict() for item in api_food_security.items]
                    )
                    total_items = api_food_security.total_items
                    print("Fetching page %s" % page)
                    max_item = page * page_size
                    time.sleep(1)
                except ApiException as e:
                    print("Exception when calling Food security data->food_security_list_get: %s\n" % e)
        df = pd.DataFrame(responses)
        return df
        

    




if __name__ == "__main__":
    pass
