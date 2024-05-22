# data_bridges_client.MarketPricesApi

<<<<<<< HEAD
All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.1.0*
=======
All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.0.0*
>>>>>>> dev

Method | HTTP request | Description
------------- | ------------- | -------------
[**market_prices_alps_get**](MarketPricesApi.md#market_prices_alps_get) | **GET** /MarketPrices/Alps | Returns time series values of ALPS and PEWI.
[**market_prices_price_daily_get**](MarketPricesApi.md#market_prices_price_daily_get) | **GET** /MarketPrices/PriceDaily | Returns a daily time series of commodity market prices.
[**market_prices_price_monthly_get**](MarketPricesApi.md#market_prices_price_monthly_get) | **GET** /MarketPrices/PriceMonthly | Returns a monthly time series of commodity market prices.
[**market_prices_price_raw_get**](MarketPricesApi.md#market_prices_price_raw_get) | **GET** /MarketPrices/PriceRaw | Returns original commodity market prices
[**market_prices_price_weekly_get**](MarketPricesApi.md#market_prices_price_weekly_get) | **GET** /MarketPrices/PriceWeekly | Returns a weekly time series of commodity market prices.


# **market_prices_alps_get**
> ViewExtendedAlpsValuePagedResult market_prices_alps_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)

Returns time series values of ALPS and PEWI.

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_marketprices-alps_get\"  Returns the full time series of the Alert for Price Spikes (ALPS) and the value of the Price Early Warning Index (PEWI). Methodology is available in [DataViz](https://dataviz.vam.wfp.org/) and [VAM-Resource Centre](https://resources.vam.wfp.org/). Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_marketprices-alps_get\"  Returns the full time series of the Alert for Price Spikes (ALPS) and the value of the Price Early Warning Index (PEWI). Methodology is available in [DataViz](https://dataviz.vam.wfp.org/) and [VAM-Resource Centre](https://resources.vam.wfp.org/). Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.view_extended_alps_value_paged_result import ViewExtendedAlpsValuePagedResult
from data_bridges_client.rest import ApiException
from pprint import pprint

<<<<<<< HEAD
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.1.0"
=======
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.0.0"
>>>>>>> dev
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.MarketPricesApi(api_client)
    country_code = 'country_code_example' # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    market_id = 0 # int | Unique ID of a Market, as found in /Markets/GeoJSONList (optional) (default to 0)
    commodity_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List (optional) (default to 0)
    price_type_name = '' # str | Price type: [retail|wholesale|farmgate] (optional) (default to '')
    currency_id = 0 # int | The exact ID of a currency, as found in /Currency/List (optional) (default to 0)
    price_flag = '' # str | Type of price data: [actual|aggregate|estimated|forecasted] (optional) (default to '')
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    latest_value_only = False # bool | [TRUE|FALSE] (optional) (default to False)
    page = 1 # int | Page number for paged results (optional) (default to 1)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Returns time series values of ALPS and PEWI.
        api_response = api_instance.market_prices_alps_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)
        print("The response of MarketPricesApi->market_prices_alps_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketPricesApi->market_prices_alps_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional] 
 **market_id** | **int**| Unique ID of a Market, as found in /Markets/GeoJSONList | [optional] [default to 0]
 **commodity_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List | [optional] [default to 0]
 **price_type_name** | **str**| Price type: [retail|wholesale|farmgate] | [optional] [default to &#39;&#39;]
 **currency_id** | **int**| The exact ID of a currency, as found in /Currency/List | [optional] [default to 0]
 **price_flag** | **str**| Type of price data: [actual|aggregate|estimated|forecasted] | [optional] [default to &#39;&#39;]
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **latest_value_only** | **bool**| [TRUE|FALSE] | [optional] [default to False]
 **page** | **int**| Page number for paged results | [optional] [default to 1]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**ViewExtendedAlpsValuePagedResult**](ViewExtendedAlpsValuePagedResult.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_prices_price_daily_get**
> ViewExtendedAggregatedPricePagedResult market_prices_price_daily_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)

Returns a daily time series of commodity market prices.

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_marketprices-pricedaily_get\"  This is the highest frequency available. Data is flagged according to its pre-processing characteristics.  Actual data is collected originally with daily frequency; aggregated data returns an empty list; imputed data is an estimation of missing values in the time series, obtained through the R Amelia-II package;        forecasted data is a six months prediction obtained through different methods, which are reported in the API.  For country specific meta-data please refer to documentation available in DataLibrary. For specific methodological notes on forecasts and imputations refer to the dedicated page in DataViz.  Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_marketprices-pricedaily_get\"  This is the highest frequency available. Data is flagged according to its pre-processing characteristics.  Actual data is collected originally with daily frequency; aggregated data returns an empty list; imputed data is an estimation of missing values in the time series, obtained through the R Amelia-II package;        forecasted data is a six months prediction obtained through different methods, which are reported in the API.  For country specific meta-data please refer to documentation available in DataLibrary. For specific methodological notes on forecasts and imputations refer to the dedicated page in DataViz.  Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.view_extended_aggregated_price_paged_result import ViewExtendedAggregatedPricePagedResult
from data_bridges_client.rest import ApiException
from pprint import pprint

<<<<<<< HEAD
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.1.0"
=======
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.0.0"
>>>>>>> dev
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.MarketPricesApi(api_client)
    country_code = 'country_code_example' # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    market_id = 0 # int | Unique ID of a Market, as found in /Markets/GeoJSONList (optional) (default to 0)
    commodity_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List (optional) (default to 0)
    price_type_name = '' # str | Price type: [retail|wholesale|farmgate] (optional) (default to '')
    currency_id = 0 # int | The exact ID of a currency, as found in /Currency/List (optional) (default to 0)
    price_flag = '' # str | Type of price data: [actual|aggregate|estimated|forecasted] (optional) (default to '')
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    latest_value_only = False # bool | [TRUE|FALSE] (optional) (default to False)
    page = 1 # int | Page number for paged results (optional) (default to 1)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Returns a daily time series of commodity market prices.
        api_response = api_instance.market_prices_price_daily_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)
        print("The response of MarketPricesApi->market_prices_price_daily_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketPricesApi->market_prices_price_daily_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional] 
 **market_id** | **int**| Unique ID of a Market, as found in /Markets/GeoJSONList | [optional] [default to 0]
 **commodity_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List | [optional] [default to 0]
 **price_type_name** | **str**| Price type: [retail|wholesale|farmgate] | [optional] [default to &#39;&#39;]
 **currency_id** | **int**| The exact ID of a currency, as found in /Currency/List | [optional] [default to 0]
 **price_flag** | **str**| Type of price data: [actual|aggregate|estimated|forecasted] | [optional] [default to &#39;&#39;]
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **latest_value_only** | **bool**| [TRUE|FALSE] | [optional] [default to False]
 **page** | **int**| Page number for paged results | [optional] [default to 1]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**ViewExtendedAggregatedPricePagedResult**](ViewExtendedAggregatedPricePagedResult.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_prices_price_monthly_get**
> ViewExtendedAggregatedPricePagedResult market_prices_price_monthly_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)

Returns a monthly time series of commodity market prices.

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_marketprices-pricemonthly_get\"  This is the lowest frequency available and the most complete data source. Data is flagged according to its pre-processing characteristics. actual data is collected originally with monthly frequency; aggregated data is collected with higher frequency (daily or weekly) averaged through a weighted mean to monthly; imputed data is an estimation of missing values in the time series, obtained through the R Amelia-II package; forecasted data is a six months prediction obtained through different methods, which are reported in the API. For country specific meta-data please refer to documentation available in [DataLibrary](https://datalib.vam.wfp.org/). For specific methodological notes on forecasts and imputations refer to the dedicated page in [DataViz](https://dataviz.vam.wfp.org/). Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_marketprices-pricemonthly_get\"  This is the lowest frequency available and the most complete data source. Data is flagged according to its pre-processing characteristics. actual data is collected originally with monthly frequency; aggregated data is collected with higher frequency (daily or weekly) averaged through a weighted mean to monthly; imputed data is an estimation of missing values in the time series, obtained through the R Amelia-II package; forecasted data is a six months prediction obtained through different methods, which are reported in the API. For country specific meta-data please refer to documentation available in [DataLibrary](https://datalib.vam.wfp.org/). For specific methodological notes on forecasts and imputations refer to the dedicated page in [DataViz](https://dataviz.vam.wfp.org/). Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.view_extended_aggregated_price_paged_result import ViewExtendedAggregatedPricePagedResult
from data_bridges_client.rest import ApiException
from pprint import pprint

<<<<<<< HEAD
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.1.0"
=======
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.0.0"
>>>>>>> dev
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.MarketPricesApi(api_client)
    country_code = 'country_code_example' # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    market_id = 0 # int | Unique ID of a Market, as found in /Markets/GeoJSONList (optional) (default to 0)
    commodity_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List (optional) (default to 0)
    price_type_name = '' # str | Price type: [retail|wholesale|farmgate] (optional) (default to '')
    currency_id = 0 # int | The exact ID of a currency, as found in /Currency/List (optional) (default to 0)
    price_flag = '' # str | Type of price data: [actual|aggregate|estimated|forecasted] (optional) (default to '')
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    latest_value_only = False # bool | [TRUE|FALSE] (optional) (default to False)
    page = 1 # int | Page number for paged results (optional) (default to 1)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Returns a monthly time series of commodity market prices.
        api_response = api_instance.market_prices_price_monthly_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)
        print("The response of MarketPricesApi->market_prices_price_monthly_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketPricesApi->market_prices_price_monthly_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional] 
 **market_id** | **int**| Unique ID of a Market, as found in /Markets/GeoJSONList | [optional] [default to 0]
 **commodity_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List | [optional] [default to 0]
 **price_type_name** | **str**| Price type: [retail|wholesale|farmgate] | [optional] [default to &#39;&#39;]
 **currency_id** | **int**| The exact ID of a currency, as found in /Currency/List | [optional] [default to 0]
 **price_flag** | **str**| Type of price data: [actual|aggregate|estimated|forecasted] | [optional] [default to &#39;&#39;]
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **latest_value_only** | **bool**| [TRUE|FALSE] | [optional] [default to False]
 **page** | **int**| Page number for paged results | [optional] [default to 1]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**ViewExtendedAggregatedPricePagedResult**](ViewExtendedAggregatedPricePagedResult.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_prices_price_raw_get**
> PagedCommodityPriceListDTO market_prices_price_raw_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)

Returns original commodity market prices

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-TEC_Architecture_+_Service_Owner_approvals_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Official%20Use%20Only-yellow)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_marketprices-priceraw_get\"  Restricted endpoint. Returns the original data with the entire Commodity Price Metadata as inserted by the focal point, which might contain sensitive or personal informatio. Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Restricted-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Official%20Use%20Only-yellow)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_marketprices-priceraw_get\"  Restricted endpoint. Returns the original data with the entire Commodity Price Metadata as inserted by the focal point, which might contain sensitive or personal informatio. Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_commodity_price_list_dto import PagedCommodityPriceListDTO
from data_bridges_client.rest import ApiException
from pprint import pprint

<<<<<<< HEAD
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.1.0"
=======
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.0.0"
>>>>>>> dev
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.MarketPricesApi(api_client)
    country_code = 'country_code_example' # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    market_id = 0 # int | Unique ID of a Market, as found in /Markets/GeoJSONList (optional) (default to 0)
    commodity_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List (optional) (default to 0)
    price_type_name = '' # str | Price type: [retail|wholesale|farmgate] (optional) (default to '')
    currency_id = 0 # int | The exact ID of a currency, as found in /Currency/List (optional) (default to 0)
    price_flag = '' # str | Type of price data: [actual|aggregate|estimated|forecasted] (optional) (default to '')
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    latest_value_only = False # bool | [TRUE|FALSE] (optional) (default to False)
    page = 1 # int | Page number for paged results (optional) (default to 1)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Returns original commodity market prices
        api_response = api_instance.market_prices_price_raw_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)
        print("The response of MarketPricesApi->market_prices_price_raw_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketPricesApi->market_prices_price_raw_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional] 
 **market_id** | **int**| Unique ID of a Market, as found in /Markets/GeoJSONList | [optional] [default to 0]
 **commodity_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List | [optional] [default to 0]
 **price_type_name** | **str**| Price type: [retail|wholesale|farmgate] | [optional] [default to &#39;&#39;]
 **currency_id** | **int**| The exact ID of a currency, as found in /Currency/List | [optional] [default to 0]
 **price_flag** | **str**| Type of price data: [actual|aggregate|estimated|forecasted] | [optional] [default to &#39;&#39;]
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **latest_value_only** | **bool**| [TRUE|FALSE] | [optional] [default to False]
 **page** | **int**| Page number for paged results | [optional] [default to 1]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**PagedCommodityPriceListDTO**](PagedCommodityPriceListDTO.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **market_prices_price_weekly_get**
> PagedCommodityWeeklyAggregatedPriceListDTO market_prices_price_weekly_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)

Returns a weekly time series of commodity market prices.

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_marketprices-priceweekly_get\"  Weeks used as reference are the International Organization for Standardization (ISO) week-numbering year (ISO-8601). Data is flagged according to its pre-processing characteristics. Aactual data is collected originally with weekly frequency; aggregated data is collected with higher frequency (daily) averaged through a weighted mean to weekly; imputed data is an estimation of missing values in the time series, obtained through the R Amelia-II package; forecasted data is a six months prediction obtained through different methods, which are reported in the API. For country specific meta-data please refer to documentation available in [DataLibrary](https://datalib.vam.wfp.org/). For specific methodological notes on forecasts and imputations refer to the dedicated page in [DataViz](https://dataviz.vam.wfp.org/). Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_marketprices-priceweekly_get\"  Weeks used as reference are the International Organization for Standardization (ISO) week-numbering year (ISO-8601). Data is flagged according to its pre-processing characteristics. Aactual data is collected originally with weekly frequency; aggregated data is collected with higher frequency (daily) averaged through a weighted mean to weekly; imputed data is an estimation of missing values in the time series, obtained through the R Amelia-II package; forecasted data is a six months prediction obtained through different methods, which are reported in the API. For country specific meta-data please refer to documentation available in [DataLibrary](https://datalib.vam.wfp.org/). For specific methodological notes on forecasts and imputations refer to the dedicated page in [DataViz](https://dataviz.vam.wfp.org/). Country code, either ISO-3166 Alpha 3 code or the VAM internal admin0code is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_commodity_weekly_aggregated_price_list_dto import PagedCommodityWeeklyAggregatedPriceListDTO
from data_bridges_client.rest import ApiException
from pprint import pprint

<<<<<<< HEAD
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.1.0"
=======
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.0.0"
>>>>>>> dev
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.MarketPricesApi(api_client)
    country_code = 'country_code_example' # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    market_id = 0 # int | Unique ID of a Market, as found in /Markets/GeoJSONList (optional) (default to 0)
    commodity_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List (optional) (default to 0)
    price_type_name = '' # str | Price type: [retail|wholesale|farmgate] (optional) (default to '')
    currency_id = 0 # int | The exact ID of a currency, as found in /Currency/List (optional) (default to 0)
    price_flag = '' # str | Type of price data: [actual|aggregate|estimated|forecasted] (optional) (default to '')
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    latest_value_only = False # bool | [TRUE|FALSE] (optional) (default to False)
    page = 1 # int | Page number for paged results (optional) (default to 1)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Returns a weekly time series of commodity market prices.
        api_response = api_instance.market_prices_price_weekly_get(country_code=country_code, market_id=market_id, commodity_id=commodity_id, price_type_name=price_type_name, currency_id=currency_id, price_flag=price_flag, start_date=start_date, end_date=end_date, latest_value_only=latest_value_only, page=page, format=format, env=env)
        print("The response of MarketPricesApi->market_prices_price_weekly_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketPricesApi->market_prices_price_weekly_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional] 
 **market_id** | **int**| Unique ID of a Market, as found in /Markets/GeoJSONList | [optional] [default to 0]
 **commodity_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List | [optional] [default to 0]
 **price_type_name** | **str**| Price type: [retail|wholesale|farmgate] | [optional] [default to &#39;&#39;]
 **currency_id** | **int**| The exact ID of a currency, as found in /Currency/List | [optional] [default to 0]
 **price_flag** | **str**| Type of price data: [actual|aggregate|estimated|forecasted] | [optional] [default to &#39;&#39;]
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **latest_value_only** | **bool**| [TRUE|FALSE] | [optional] [default to False]
 **page** | **int**| Page number for paged results | [optional] [default to 1]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**PagedCommodityWeeklyAggregatedPriceListDTO**](PagedCommodityWeeklyAggregatedPriceListDTO.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

