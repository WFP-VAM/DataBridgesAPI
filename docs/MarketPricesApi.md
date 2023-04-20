# data_bridges_client.MarketPricesApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/1.3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_prices_alps_get**](MarketPricesApi.md#market_prices_alps_get) | **GET** /MarketPrices/Alps | Returns time series values of ALPS and PEWI.
[**market_prices_price_daily_get**](MarketPricesApi.md#market_prices_price_daily_get) | **GET** /MarketPrices/PriceDaily | Returns a daily time series of commodity market prices.
[**market_prices_price_monthly_get**](MarketPricesApi.md#market_prices_price_monthly_get) | **GET** /MarketPrices/PriceMonthly | Returns a monthly time series of commodity market prices.
[**market_prices_price_raw_get**](MarketPricesApi.md#market_prices_price_raw_get) | **GET** /MarketPrices/PriceRaw | Returns original commodity market prices
[**market_prices_price_weekly_get**](MarketPricesApi.md#market_prices_price_weekly_get) | **GET** /MarketPrices/PriceWeekly | Returns a weekly time series of commodity market prices.


# **market_prices_alps_get**
> ViewExtendedAlpsValuePagedResult market_prices_alps_get()

Returns time series values of ALPS and PEWI.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  Returns the full time series of the Alert for Price Spikes (ALPS) and the value of the Price Early Warning Index (PEWI). Methodology is available in [DataViz](https://dataviz.vam.wfp.org/) and [VAM-Resource Centre](https://resources.vam.wfp.org/). Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import market_prices_api
from data_bridges_client.model.view_extended_alps_value_paged_result import ViewExtendedAlpsValuePagedResult
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from pprint import pprint
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/1.3.1
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.3.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: default
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.3.1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = market_prices_api.MarketPricesApi(api_client)
    country_code = "countryCode_example" # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    market_id = 0 # int | Unique ID of a Market, as found in /Markets/GeoJSONList (optional) if omitted the server will use the default value of 0
    commodity_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List (optional) if omitted the server will use the default value of 0
    price_type_name = "" # str | Price type: [retail|wholesale|farmgate] (optional) if omitted the server will use the default value of ""
    currency_id = 0 # int | The exact ID of a currency, as found in /Currency/List (optional) if omitted the server will use the default value of 0
    price_flag = "" # str | Type of price data: [actual|aggregate|estimated|forecasted] (optional) if omitted the server will use the default value of ""
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    latest_value_only = False # bool | [TRUE|FALSE] (optional) if omitted the server will use the default value of False
    page = 1 # int | Page number for paged results (optional) if omitted the server will use the default value of 1
    format = "json" # str | Output format: [JSON|CSV] Json is the default value (optional) if omitted the server will use the default value of "json"
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns time series values of ALPS and PEWI.
        api_response = api_instance.market_prices_alps_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling MarketPricesApi->market_prices_alps_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional]
 **market_id** | **int**| Unique ID of a Market, as found in /Markets/GeoJSONList | [optional] if omitted the server will use the default value of 0
 **commodity_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List | [optional] if omitted the server will use the default value of 0
 **price_type_name** | **str**| Price type: [retail|wholesale|farmgate] | [optional] if omitted the server will use the default value of ""
 **currency_id** | **int**| The exact ID of a currency, as found in /Currency/List | [optional] if omitted the server will use the default value of 0
 **price_flag** | **str**| Type of price data: [actual|aggregate|estimated|forecasted] | [optional] if omitted the server will use the default value of ""
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **latest_value_only** | **bool**| [TRUE|FALSE] | [optional] if omitted the server will use the default value of False
 **page** | **int**| Page number for paged results | [optional] if omitted the server will use the default value of 1
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] if omitted the server will use the default value of "json"
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional]

### Return type

[**ViewExtendedAlpsValuePagedResult**](ViewExtendedAlpsValuePagedResult.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_prices_price_daily_get**
> ViewExtendedAggregatedPricePagedResult market_prices_price_daily_get()

Returns a daily time series of commodity market prices.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  This is the highest frequency available. Data is flagged according to its pre-processing characteristics. Actual data is collected originally with daily frequency; aggregated data returns an empty list; imputed data is an estimation of missing values in the time series, obtained through the R Amelia-II package;        forecasted data is a six months prediction obtained through different methods, which are reported in the API.  For country specific meta-data please refer to documentation available in DataLibrary. For specific methodological notes on forecasts and imputations refer to the dedicated page in DataViz.  Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import market_prices_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.view_extended_aggregated_price_paged_result import ViewExtendedAggregatedPricePagedResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/1.3.1
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.3.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: default
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.3.1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = market_prices_api.MarketPricesApi(api_client)
    country_code = "countryCode_example" # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    market_id = 0 # int | Unique ID of a Market, as found in /Markets/GeoJSONList (optional) if omitted the server will use the default value of 0
    commodity_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List (optional) if omitted the server will use the default value of 0
    price_type_name = "" # str | Price type: [retail|wholesale|farmgate] (optional) if omitted the server will use the default value of ""
    currency_id = 0 # int | The exact ID of a currency, as found in /Currency/List (optional) if omitted the server will use the default value of 0
    price_flag = "" # str | Type of price data: [actual|aggregate|estimated|forecasted] (optional) if omitted the server will use the default value of ""
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    latest_value_only = False # bool | [TRUE|FALSE] (optional) if omitted the server will use the default value of False
    page = 1 # int | Page number for paged results (optional) if omitted the server will use the default value of 1
    format = "json" # str | Output format: [JSON|CSV] Json is the default value (optional) if omitted the server will use the default value of "json"
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a daily time series of commodity market prices.
        api_response = api_instance.market_prices_price_daily_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling MarketPricesApi->market_prices_price_daily_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional]
 **market_id** | **int**| Unique ID of a Market, as found in /Markets/GeoJSONList | [optional] if omitted the server will use the default value of 0
 **commodity_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List | [optional] if omitted the server will use the default value of 0
 **price_type_name** | **str**| Price type: [retail|wholesale|farmgate] | [optional] if omitted the server will use the default value of ""
 **currency_id** | **int**| The exact ID of a currency, as found in /Currency/List | [optional] if omitted the server will use the default value of 0
 **price_flag** | **str**| Type of price data: [actual|aggregate|estimated|forecasted] | [optional] if omitted the server will use the default value of ""
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **latest_value_only** | **bool**| [TRUE|FALSE] | [optional] if omitted the server will use the default value of False
 **page** | **int**| Page number for paged results | [optional] if omitted the server will use the default value of 1
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] if omitted the server will use the default value of "json"
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional]

### Return type

[**ViewExtendedAggregatedPricePagedResult**](ViewExtendedAggregatedPricePagedResult.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_prices_price_monthly_get**
> ViewExtendedAggregatedPricePagedResult market_prices_price_monthly_get()

Returns a monthly time series of commodity market prices.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  This is the lowest frequency available and the most complete data source. Data is flagged according to its pre-processing characteristics. actual data is collected originally with monthly frequency; aggregated data is collected with higher frequency (daily or weekly) averaged through a weighted mean to monthly; imputed data is an estimation of missing values in the time series, obtained through the R Amelia-II package; forecasted data is a six months prediction obtained through different methods, which are reported in the API. For country specific meta-data please refer to documentation available in [DataLibrary](https://datalib.vam.wfp.org/). For specific methodological notes on forecasts and imputations refer to the dedicated page in [DataViz](https://dataviz.vam.wfp.org/). Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import market_prices_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.view_extended_aggregated_price_paged_result import ViewExtendedAggregatedPricePagedResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/1.3.1
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.3.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: default
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.3.1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = market_prices_api.MarketPricesApi(api_client)
    country_code = "countryCode_example" # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    market_id = 0 # int | Unique ID of a Market, as found in /Markets/GeoJSONList (optional) if omitted the server will use the default value of 0
    commodity_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List (optional) if omitted the server will use the default value of 0
    price_type_name = "" # str | Price type: [retail|wholesale|farmgate] (optional) if omitted the server will use the default value of ""
    currency_id = 0 # int | The exact ID of a currency, as found in /Currency/List (optional) if omitted the server will use the default value of 0
    price_flag = "" # str | Type of price data: [actual|aggregate|estimated|forecasted] (optional) if omitted the server will use the default value of ""
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    latest_value_only = False # bool | [TRUE|FALSE] (optional) if omitted the server will use the default value of False
    page = 1 # int | Page number for paged results (optional) if omitted the server will use the default value of 1
    format = "json" # str | Output format: [JSON|CSV] Json is the default value (optional) if omitted the server will use the default value of "json"
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a monthly time series of commodity market prices.
        api_response = api_instance.market_prices_price_monthly_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling MarketPricesApi->market_prices_price_monthly_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional]
 **market_id** | **int**| Unique ID of a Market, as found in /Markets/GeoJSONList | [optional] if omitted the server will use the default value of 0
 **commodity_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List | [optional] if omitted the server will use the default value of 0
 **price_type_name** | **str**| Price type: [retail|wholesale|farmgate] | [optional] if omitted the server will use the default value of ""
 **currency_id** | **int**| The exact ID of a currency, as found in /Currency/List | [optional] if omitted the server will use the default value of 0
 **price_flag** | **str**| Type of price data: [actual|aggregate|estimated|forecasted] | [optional] if omitted the server will use the default value of ""
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **latest_value_only** | **bool**| [TRUE|FALSE] | [optional] if omitted the server will use the default value of False
 **page** | **int**| Page number for paged results | [optional] if omitted the server will use the default value of 1
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] if omitted the server will use the default value of "json"
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional]

### Return type

[**ViewExtendedAggregatedPricePagedResult**](ViewExtendedAggregatedPricePagedResult.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_prices_price_raw_get**
> PagedCommodityPriceListDTO market_prices_price_raw_get()

Returns original commodity market prices

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Restricted-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Official%20Use%20Only-yellow)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_marketprices-priceraw_get\"  Restricted endpoint. Returns the original data with the entire Commodity Price Metadata as inserted by the focal point, which might contain sensitive or personal informatio. Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import market_prices_api
from data_bridges_client.model.paged_commodity_price_list_dto import PagedCommodityPriceListDTO
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from pprint import pprint
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/1.3.1
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.3.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: default
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.3.1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = market_prices_api.MarketPricesApi(api_client)
    country_code = "countryCode_example" # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    market_id = 0 # int | Unique ID of a Market, as found in /Markets/GeoJSONList (optional) if omitted the server will use the default value of 0
    commodity_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List (optional) if omitted the server will use the default value of 0
    price_type_name = "" # str | Price type: [retail|wholesale|farmgate] (optional) if omitted the server will use the default value of ""
    currency_id = 0 # int | The exact ID of a currency, as found in /Currency/List (optional) if omitted the server will use the default value of 0
    price_flag = "" # str | Type of price data: [actual|aggregate|estimated|forecasted] (optional) if omitted the server will use the default value of ""
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    latest_value_only = False # bool | [TRUE|FALSE] (optional) if omitted the server will use the default value of False
    page = 1 # int | Page number for paged results (optional) if omitted the server will use the default value of 1
    format = "json" # str | Output format: [JSON|CSV] Json is the default value (optional) if omitted the server will use the default value of "json"
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns original commodity market prices
        api_response = api_instance.market_prices_price_raw_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling MarketPricesApi->market_prices_price_raw_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional]
 **market_id** | **int**| Unique ID of a Market, as found in /Markets/GeoJSONList | [optional] if omitted the server will use the default value of 0
 **commodity_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List | [optional] if omitted the server will use the default value of 0
 **price_type_name** | **str**| Price type: [retail|wholesale|farmgate] | [optional] if omitted the server will use the default value of ""
 **currency_id** | **int**| The exact ID of a currency, as found in /Currency/List | [optional] if omitted the server will use the default value of 0
 **price_flag** | **str**| Type of price data: [actual|aggregate|estimated|forecasted] | [optional] if omitted the server will use the default value of ""
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **latest_value_only** | **bool**| [TRUE|FALSE] | [optional] if omitted the server will use the default value of False
 **page** | **int**| Page number for paged results | [optional] if omitted the server will use the default value of 1
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] if omitted the server will use the default value of "json"
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional]

### Return type

[**PagedCommodityPriceListDTO**](PagedCommodityPriceListDTO.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_prices_price_weekly_get**
> PagedCommodityWeeklyAggregatedPriceListDTO market_prices_price_weekly_get()

Returns a weekly time series of commodity market prices.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  Weeks used as reference are the International Organization for Standardization (ISO) week-numbering year (ISO-8601). Data is flagged according to its pre-processing characteristics. Aactual data is collected originally with weekly frequency; aggregated data is collected with higher frequency (daily) averaged through a weighted mean to weekly; imputed data is an estimation of missing values in the time series, obtained through the R Amelia-II package; forecasted data is a six months prediction obtained through different methods, which are reported in the API. For country specific meta-data please refer to documentation available in [DataLibrary](https://datalib.vam.wfp.org/). For specific methodological notes on forecasts and imputations refer to the dedicated page in [DataViz](https://dataviz.vam.wfp.org/). Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import market_prices_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.paged_commodity_weekly_aggregated_price_list_dto import PagedCommodityWeeklyAggregatedPriceListDTO
from pprint import pprint
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/1.3.1
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.3.1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: default
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.3.1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = market_prices_api.MarketPricesApi(api_client)
    country_code = "countryCode_example" # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    market_id = 0 # int | Unique ID of a Market, as found in /Markets/GeoJSONList (optional) if omitted the server will use the default value of 0
    commodity_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List (optional) if omitted the server will use the default value of 0
    price_type_name = "" # str | Price type: [retail|wholesale|farmgate] (optional) if omitted the server will use the default value of ""
    currency_id = 0 # int | The exact ID of a currency, as found in /Currency/List (optional) if omitted the server will use the default value of 0
    price_flag = "" # str | Type of price data: [actual|aggregate|estimated|forecasted] (optional) if omitted the server will use the default value of ""
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    latest_value_only = False # bool | [TRUE|FALSE] (optional) if omitted the server will use the default value of False
    page = 1 # int | Page number for paged results (optional) if omitted the server will use the default value of 1
    format = "json" # str | Output format: [JSON|CSV] Json is the default value (optional) if omitted the server will use the default value of "json"
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a weekly time series of commodity market prices.
        api_response = api_instance.market_prices_price_weekly_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling MarketPricesApi->market_prices_price_weekly_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional]
 **market_id** | **int**| Unique ID of a Market, as found in /Markets/GeoJSONList | [optional] if omitted the server will use the default value of 0
 **commodity_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List | [optional] if omitted the server will use the default value of 0
 **price_type_name** | **str**| Price type: [retail|wholesale|farmgate] | [optional] if omitted the server will use the default value of ""
 **currency_id** | **int**| The exact ID of a currency, as found in /Currency/List | [optional] if omitted the server will use the default value of 0
 **price_flag** | **str**| Type of price data: [actual|aggregate|estimated|forecasted] | [optional] if omitted the server will use the default value of ""
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **latest_value_only** | **bool**| [TRUE|FALSE] | [optional] if omitted the server will use the default value of False
 **page** | **int**| Page number for paged results | [optional] if omitted the server will use the default value of 1
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] if omitted the server will use the default value of "json"
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional]

### Return type

[**PagedCommodityWeeklyAggregatedPriceListDTO**](PagedCommodityWeeklyAggregatedPriceListDTO.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

