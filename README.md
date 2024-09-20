# data-bridges-client
API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 5.0.0
- Package version: 5.0.0
- Generator version: 7.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/WFP-VAM/DataBridgesAPI.git@release/v5.0
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/WFP-VAM/DataBridgesAPI.git`)

Then import the package:
```python
import data_bridges_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import data_bridges_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import data_bridges_client
from data_bridges_client.rest import ApiException
from data_bridges_client.token import WfpApiToken
from pprint import pprint

# Configure OAuth2 access token for authorization: default
KEY = ''
SECRET = ''
SCOPES = ['', '']
token = WfpApiToken(api_key=KEY, api_secret=SECRET)

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/1.4.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/5.0.0"
)
configuration.access_token = token.refresh(scopes=SCOPES)

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.CommoditiesApi(api_client)
    country_code = 'country_code_example' # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code (optional)
    category_name = 'category_name_example' # str | The name, even partial and case insensitive, of a commodity category. (optional)
    category_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List. (optional) (default to 0)
    page = 1 # int | page number for paged results (optional) (default to 1)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Provides the list of categories.
        api_response = api_instance.commodities_categories_list_get(country_code=country_code, category_name=category_name, category_id=category_id, page=page, format=format, env=env)
        print("The response of CommoditiesApi->commodities_categories_list_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommoditiesApi->commodities_categories_list_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.wfp.org/vam-data-bridges/5.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CommoditiesApi* | [**commodities_categories_list_get**](docs/CommoditiesApi.md#commodities_categories_list_get) | **GET** /Commodities/Categories/List | Provides the list of categories.
*CommoditiesApi* | [**commodities_list_get**](docs/CommoditiesApi.md#commodities_list_get) | **GET** /Commodities/List | Provide the detailed list of the commodities available in DataBridges platform
*CommodityUnitsApi* | [**commodity_units_conversion_list_get**](docs/CommodityUnitsApi.md#commodity_units_conversion_list_get) | **GET** /CommodityUnits/Conversion/List | Provides conversion factors to Kilogram or Litres for each convertible unit of measure.
*CommodityUnitsApi* | [**commodity_units_list_get**](docs/CommodityUnitsApi.md#commodity_units_list_get) | **GET** /CommodityUnits/List | Provides the detailed list of the unit of measure available in DataBridges platform
*CurrencyApi* | [**currency_list_get**](docs/CurrencyApi.md#currency_list_get) | **GET** /Currency/List | Returns the list of currencies available in the internal VAM database, with Currency 3-letter code, matching with ISO 4217.
*CurrencyApi* | [**currency_usd_indirect_quotation_get**](docs/CurrencyApi.md#currency_usd_indirect_quotation_get) | **GET** /Currency/UsdIndirectQuotation | Returns the value of the Exchange rates from Trading Economics, for official rates, and DataViz for unofficial rates.
*EconomicDataApi* | [**economic_data_indicator_list_get**](docs/EconomicDataApi.md#economic_data_indicator_list_get) | **GET** /EconomicData/IndicatorList | Returns the lists of indicators.
*EconomicDataApi* | [**economic_data_indicator_name_get**](docs/EconomicDataApi.md#economic_data_indicator_name_get) | **GET** /EconomicData/{indicatorName} | Returns the time series of values for different indicators.
*FoodSecurityApi* | [**food_security_list_get**](docs/FoodSecurityApi.md#food_security_list_get) | **GET** /FoodSecurity/List | 
*GorpApi* | [**gorp_latest_get**](docs/GorpApi.md#gorp_latest_get) | **GET** /Gorp/Latest | Return the latest dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.
*GorpApi* | [**gorp_list_get**](docs/GorpApi.md#gorp_list_get) | **GET** /Gorp/List | Return the full dataset of number of acutely food insecure (in millions) based on WFP Global Operational Response Plan.
*IncubationApi* | [**household_draft_internal_base_data_get**](docs/IncubationApi.md#household_draft_internal_base_data_get) | **GET** /Household/DraftInternalBaseData | Get data that includes the core household fields only by Survey ID
*IncubationApi* | [**household_full_data_get**](docs/IncubationApi.md#household_full_data_get) | **GET** /Household/FullData | Get a full dataset that includes all the fields included in the survey in addition to the core household fields by Survey ID. To access this data, please contact xxxx for authorization.
*IncubationApi* | [**household_official_use_base_data_get**](docs/IncubationApi.md#household_official_use_base_data_get) | **GET** /Household/OfficialUseBaseData | Get data that includes the core household fields only by Survey ID
*IncubationApi* | [**household_public_base_data_get**](docs/IncubationApi.md#household_public_base_data_get) | **GET** /Household/PublicBaseData | Get data that includes the core household fields only by Survey ID
*IncubationApi* | [**household_surveys_get**](docs/IncubationApi.md#household_surveys_get) | **GET** /Household/Surveys | Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all household surveys conducted in a country.   A date of reference, SurveyDate, for the data collection is set by the officer responsible for the upload for each survey.
*IncubationApi* | [**xls_forms_definition_get**](docs/IncubationApi.md#xls_forms_definition_get) | **GET** /XlsForms/definition | Get a complete set of XLS Form definitions of a given XLS Form ID. This is the digital version of the questionnaire used during the data collection exercise.
*MarketPricesApi* | [**market_prices_alps_get**](docs/MarketPricesApi.md#market_prices_alps_get) | **GET** /MarketPrices/Alps | Returns time series values of ALPS and PEWI.
*MarketPricesApi* | [**market_prices_price_daily_get**](docs/MarketPricesApi.md#market_prices_price_daily_get) | **GET** /MarketPrices/PriceDaily | Returns a daily time series of commodity market prices.
*MarketPricesApi* | [**market_prices_price_monthly_get**](docs/MarketPricesApi.md#market_prices_price_monthly_get) | **GET** /MarketPrices/PriceMonthly | Returns a monthly time series of commodity market prices.
*MarketPricesApi* | [**market_prices_price_raw_get**](docs/MarketPricesApi.md#market_prices_price_raw_get) | **GET** /MarketPrices/PriceRaw | Returns original commodity market prices
*MarketPricesApi* | [**market_prices_price_weekly_get**](docs/MarketPricesApi.md#market_prices_price_weekly_get) | **GET** /MarketPrices/PriceWeekly | Returns a weekly time series of commodity market prices.
*MarketsApi* | [**markets_geo_json_list_get**](docs/MarketsApi.md#markets_geo_json_list_get) | **GET** /Markets/GeoJSONList | Provide a list of geo referenced markets in a specific country
*MarketsApi* | [**markets_list_get**](docs/MarketsApi.md#markets_list_get) | **GET** /Markets/List | Get a complete list of markets in a country
*MarketsApi* | [**markets_markets_as_csv_get**](docs/MarketsApi.md#markets_markets_as_csv_get) | **GET** /Markets/MarketsAsCSV | Get a complete list of markets in a country
*MarketsApi* | [**markets_nearby_markets_get**](docs/MarketsApi.md#markets_nearby_markets_get) | **GET** /Markets/NearbyMarkets | Find markets near a given location by longitude and latitude within a 15Km distance
*RpmeApi* | [**rpme_base_data_get**](docs/RpmeApi.md#rpme_base_data_get) | **GET** /Rpme/BaseData | Get data that includes the core RPME fields only by Survey ID
*RpmeApi* | [**rpme_full_data_get**](docs/RpmeApi.md#rpme_full_data_get) | **GET** /Rpme/FullData | Get a full dataset that includes all the fields included in the survey in addition to the core RPME fields by Survey ID.
*RpmeApi* | [**rpme_output_values_get**](docs/RpmeApi.md#rpme_output_values_get) | **GET** /Rpme/OutputValues | Processed values for each variable used in the assessments
*RpmeApi* | [**rpme_surveys_get**](docs/RpmeApi.md#rpme_surveys_get) | **GET** /Rpme/Surveys | Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all RPME surveys conducted in a country. The date of reference, SurveyDate, for the data collection is set by the officer responsible for the upload of each survey.
*RpmeApi* | [**rpme_variables_get**](docs/RpmeApi.md#rpme_variables_get) | **GET** /Rpme/Variables | List of variables
*RpmeApi* | [**rpme_xls_forms_get**](docs/RpmeApi.md#rpme_xls_forms_get) | **GET** /Rpme/XLSForms | Get a complete list of XLS Forms uploaded on the RPME in a given period of data collection. This is the digital version of the questionnaire used during the data collection exercise.
*SurveysApi* | [**m_fi_surveys_base_data_get**](docs/SurveysApi.md#m_fi_surveys_base_data_get) | **GET** /MFI/Surveys/BaseData | Get data that includes the core Market Functionality Index (MFI) fields only by Survey ID
*SurveysApi* | [**m_fi_surveys_full_data_get**](docs/SurveysApi.md#m_fi_surveys_full_data_get) | **GET** /MFI/Surveys/FullData | Get a full dataset that includes all the fields included in the survey in addition to the core Market Functionality Index (MFI) fields by Survey ID. To access this data, please contact global.mfi@wfp.org for authorization.
*SurveysApi* | [**m_fi_surveys_get**](docs/SurveysApi.md#m_fi_surveys_get) | **GET** /MFI/Surveys | Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all MFI surveys conducted in a country.   A date of reference, SurveyDate, for the data collection is set by the officer responsible for the upload for each survey.
*SurveysApi* | [**m_fi_surveys_processed_data_get**](docs/SurveysApi.md#m_fi_surveys_processed_data_get) | **GET** /MFI/Surveys/ProcessedData | Get a MFI processed data in long format; levels indicate the data aggregation level 1) Normalized Score, 2) Trader Aggregate Score,   3) Market Aggregate Score, 4) Trader Median, 5) Trader Mean, 6) Market Mean; each line corresponds to one of the nine dimensions of scores   plus the final MFI aggregate score; 1) Assortment, 2) Availability, 3) Price, 4) Resilience, 5) Competition, 6) Infrastructure, 7) Service,   8) Quality, 9) Access and Protection, and 10) MFI final score; the variable label describes each variable and its value range
*XlsFormsApi* | [**m_fi_xls_forms_get**](docs/XlsFormsApi.md#m_fi_xls_forms_get) | **GET** /MFI/XlsForms | Get a complete list of XLS Forms uploaded on the MFI Data Bridge in a given period of data collection. This is the digital version of the questionnaire used during the data collection exercise.


## Documentation For Models

 - [BadRequestDTO](docs/BadRequestDTO.md)
 - [CommodityDTO](docs/CommodityDTO.md)
 - [CommodityPriceDTO](docs/CommodityPriceDTO.md)
 - [CommodityProcessingDTO](docs/CommodityProcessingDTO.md)
 - [CommodityQualityDTO](docs/CommodityQualityDTO.md)
 - [CurrencyDTO](docs/CurrencyDTO.md)
 - [EconomicDataDTO](docs/EconomicDataDTO.md)
 - [EconomicIndicatorProperty](docs/EconomicIndicatorProperty.md)
 - [EconomicIndicatorPropertyPagedResult](docs/EconomicIndicatorPropertyPagedResult.md)
 - [Feature](docs/Feature.md)
 - [Geometry](docs/Geometry.md)
 - [GorpValueWithChanges](docs/GorpValueWithChanges.md)
 - [GorpValueWithChangesPagedResult](docs/GorpValueWithChangesPagedResult.md)
 - [HouseholdSurveyListDTO](docs/HouseholdSurveyListDTO.md)
 - [HouseholdSurveyListDTOPagedResult](docs/HouseholdSurveyListDTOPagedResult.md)
 - [IpcValue](docs/IpcValue.md)
 - [IpcValuePagedResult](docs/IpcValuePagedResult.md)
 - [KeyNameDto](docs/KeyNameDto.md)
 - [MFIProcessedDataDTO](docs/MFIProcessedDataDTO.md)
 - [MarketDTO](docs/MarketDTO.md)
 - [MarketGeoJsonRoot](docs/MarketGeoJsonRoot.md)
 - [NearbyMarketsDTO](docs/NearbyMarketsDTO.md)
 - [PagedCommodityListDTO](docs/PagedCommodityListDTO.md)
 - [PagedCommodityPriceListDTO](docs/PagedCommodityPriceListDTO.md)
 - [PagedCommodityWeeklyAggregatedPriceListDTO](docs/PagedCommodityWeeklyAggregatedPriceListDTO.md)
 - [PagedCurrencyListDTO](docs/PagedCurrencyListDTO.md)
 - [PagedEconomicDataDTO](docs/PagedEconomicDataDTO.md)
 - [PagedMarketListDTO](docs/PagedMarketListDTO.md)
 - [PagedProcessedDataDTO](docs/PagedProcessedDataDTO.md)
 - [PagedSurveyListDTO](docs/PagedSurveyListDTO.md)
 - [PagedSurveyResponsesDTO](docs/PagedSurveyResponsesDTO.md)
 - [PagedXlsFormListDTO](docs/PagedXlsFormListDTO.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [Properties](docs/Properties.md)
 - [RpmeAssessment](docs/RpmeAssessment.md)
 - [RpmeAssessmentPagedResult](docs/RpmeAssessmentPagedResult.md)
 - [RpmeOutputValues](docs/RpmeOutputValues.md)
 - [RpmeVariable](docs/RpmeVariable.md)
 - [RpmeVariablePagedResult](docs/RpmeVariablePagedResult.md)
 - [SurveyListDTO](docs/SurveyListDTO.md)
 - [UsdIndirectQuotation](docs/UsdIndirectQuotation.md)
 - [UsdIndirectQuotationPagedResult](docs/UsdIndirectQuotationPagedResult.md)
 - [ViewExtendedAggregatedPrice](docs/ViewExtendedAggregatedPrice.md)
 - [ViewExtendedAggregatedPricePagedResult](docs/ViewExtendedAggregatedPricePagedResult.md)
 - [ViewExtendedAlpsValue](docs/ViewExtendedAlpsValue.md)
 - [ViewExtendedAlpsValuePagedResult](docs/ViewExtendedAlpsValuePagedResult.md)
 - [WeeklyAggregatedPrice](docs/WeeklyAggregatedPrice.md)
 - [XlsFormDTO](docs/XlsFormDTO.md)
 - [XlsFormDefinitionNewSchemaDTO](docs/XlsFormDefinitionNewSchemaDTO.md)
 - [XlsFormFieldsDTO](docs/XlsFormFieldsDTO.md)
 - [XlsFormListChoiceDTO](docs/XlsFormListChoiceDTO.md)
 - [XlsFormListChoicesDTO](docs/XlsFormListChoicesDTO.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="default"></a>
### default

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://api.wfp.org/authorize
- **Scopes**: 
 - **vamdatabridges_rpme-fulldata_get**: vamdatabridges_rpme-fulldata_get
 - **vamdatabridges_foodsecurity-list_get**: vamdatabridges_foodsecurity-list_get
 - **vamdatabridges_commodities-list_get**: vamdatabridges_commodities-list_get
 - **vamdatabridges_commodityunits-list_get**: vamdatabridges_commodityunits-list_get
 - **vamdatabridges_markets-nearbymarkets_get**: vamdatabridges_markets-nearbymarkets_get
 - **vamdatabridges_rpme-outputvalues_get**: vamdatabridges_rpme-outputvalues_get
 - **vamdatabridges_marketprices-alps_get**: vamdatabridges_marketprices-alps_get
 - **vamdatabridges_mfi-surveys_get**: vamdatabridges_mfi-surveys_get
 - **vamdatabridges_commodities-categories-list_get**: vamdatabridges_commodities-categories-list_get
 - **vamdatabridges_commodityunits-conversion-list_get**: vamdatabridges_commodityunits-conversion-list_get
 - **vamdatabridges_economicdata_get**: vamdatabridges_economicdata_get
 - **vamdatabridges_mfi-surveys-processeddata_get**: vamdatabridges_mfi-surveys-processeddata_get
 - **vamdatabridges_marketprices-priceweekly_get**: vamdatabridges_marketprices-priceweekly_get
 - **vamdatabridges_markets-marketsascsv_get**: vamdatabridges_markets-marketsascsv_get
 - **vamdatabridges_household-publicbasedata_get**: vamdatabridges_household-publicbasedata_get
 - **vamdatabridges_mfi-xlsforms_get**: vamdatabridges_mfi-xlsforms_get
 - **vamdatabridges_economicdata-indicatorlist_get**: vamdatabridges_economicdata-indicatorlist_get
 - **vamdatabridges_markets-geojsonlist_get**: vamdatabridges_markets-geojsonlist_get
 - **vamdatabridges_rpme-surveys_get**: vamdatabridges_rpme-surveys_get
 - **vamdatabridges_rpme-xlsforms_get**: vamdatabridges_rpme-xlsforms_get
 - **vamdatabridges_mfi-surveys-basedata_get**: vamdatabridges_mfi-surveys-basedata_get
 - **vamdatabridges_mfi-surveys-fulldata_get**: vamdatabridges_mfi-surveys-fulldata_get
 - **vamdatabridges_household-fulldata_get**: vamdatabridges_household-fulldata_get
 - **vamdatabridges_household-officialusebasedata_get**: vamdatabridges_household-officialusebasedata_get
 - **vamdatabridges_marketprices-pricemonthly_get**: vamdatabridges_marketprices-pricemonthly_get
 - **vamdatabridges_markets-list_get**: vamdatabridges_markets-list_get
 - **vamdatabridges_currency-list_get**: vamdatabridges_currency-list_get
 - **vamdatabridges_gorp-list_get**: vamdatabridges_gorp-list_get
 - **vamdatabridges_marketprices-priceraw_get**: vamdatabridges_marketprices-priceraw_get
 - **vamdatabridges_rpme-variables_get**: vamdatabridges_rpme-variables_get
 - **vamdatabridges_gorp-latest_get**: vamdatabridges_gorp-latest_get
 - **vamdatabridges_currency-usdindirectquotation_get**: vamdatabridges_currency-usdindirectquotation_get
 - **vamdatabridges_xlsforms-definition_get**: vamdatabridges_xlsforms-definition_get
 - **vamdatabridges_household-draftinternalbasedata_get**: vamdatabridges_household-draftinternalbasedata_get
 - **vamdatabridges_household-surveys_get**: vamdatabridges_household-surveys_get
 - **vamdatabridges_marketprices-pricedaily_get**: vamdatabridges_marketprices-pricedaily_get
 - **vamdatabridges_rpme-basedata_get**: vamdatabridges_rpme-basedata_get


## Author

wfp.economicanalysis@wfp.org


