import time
import data_bridges_client
from data_bridges_client.rest import ApiException
from pprint import pprint
from data_bridges_client.token import WfpApiToken
import yaml
import os
from datetime import timedelta
from datetime import date
import pandas


def setup_configuration_and_authentication(yamlpath):
    """Loads configuration from a YAML file and sets up authentication."""

    with open(yamlpath, "r") as yamlfile:
        databridges_config = yaml.load(yamlfile, Loader=yaml.FullLoader)
        print("Read successful")

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


def shapes_get_survey(surveyid, yamlpath, access_type, page_size=200):
    """Retrieves survey data using the specified configuration and access type."""

    configuration = setup_configuration_and_authentication(yamlpath)

    responses = []
    page_size = page_size
    total_items = 1
    max_item = 0
    page = 0

    while total_items > max_item:
        page += 1
        with data_bridges_client.ApiClient(configuration) as api_client:
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
                }.get(access_type)(survey_id=surveyid, page=page, env=env)
                print("Fetching page %s" % page)
                print("items - %s" % str(len(api_survey.items)))
                responses.extend(
                    [item for item in api_survey.items]
                )
                total_items = api_survey.total_items
                max_item = len(api_survey.items) + max_item
                time.sleep(1)

            except ApiException as e:
                print("Exception when calling Household data->" % access_type % ": %s\n" % e)

    responses = pandas.DataFrame(responses)
    return responses


def shapes_get_prices(country_iso3, yamlpath, survey_date, page_size=1000):

    configuration = setup_configuration_and_authentication(yamlpath)

    if survey_date != '':
        start_date = date.fromisoformat(survey_date) - timedelta(days=365)
    else:
        start_date = date.fromisocalendar(1990, 1, 1)
    responses = []
    # Enter a context with an instance of the API client
    page_size = page_size
    total_items = 20
    max_item = 0
    page = 0
    while total_items > max_item:
        page = page + 1  # int | page number for paged results (optional) (default to 1)
        with data_bridges_client.ApiClient(configuration) as api_client:
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
    responses = pandas.DataFrame(responses)
    return responses


def shapes_get_exchangerates(country_iso3, yamlpath, page_size=1000):

    configuration = setup_configuration_and_authentication(yamlpath)

    responses = []

    # Enter a context with an instance of the API client
    page_size = page_size
    total_items = 20
    max_item = 0
    page = 0
    while total_items > max_item:
        page = page + 1  # int | page number for paged results (optional) (default to 1)
        with data_bridges_client.ApiClient(configuration) as api_client:
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
    responses = pandas.DataFrame(responses)
    return responses