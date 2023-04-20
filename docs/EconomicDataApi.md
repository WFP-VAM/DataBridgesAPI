# data_bridges_client.EconomicDataApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/1.3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**economic_data_indicator_list_get**](EconomicDataApi.md#economic_data_indicator_list_get) | **GET** /EconomicData/IndicatorList | Returns the lists of indicators.
[**economic_data_indicator_name_get**](EconomicDataApi.md#economic_data_indicator_name_get) | **GET** /EconomicData/{indicatorName} | Returns the time series of values for different indicators.


# **economic_data_indicator_list_get**
> EconomicIndicatorPropertyPagedResult economic_data_indicator_list_get()

Returns the lists of indicators.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  Returns the lists of indicators for which Vulnerability Analysis and Mapping - Economic and Market Analysis Unit has redistribution licensing from Trading Economics. No mandatory parameter.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import economic_data_api
from data_bridges_client.model.problem_details import ProblemDetails
from data_bridges_client.model.economic_indicator_property_paged_result import EconomicIndicatorPropertyPagedResult
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
    api_instance = economic_data_api.EconomicDataApi(api_client)
    page = 1 # int | Page number for paged results (optional) if omitted the server will use the default value of 1
    indicator_name = "" # str | Unique indicator name. (optional) if omitted the server will use the default value of ""
    iso3 = "" # str | The code to identify the country. Must be a ISO-3166 Alpha 3 code. (optional) if omitted the server will use the default value of ""
    format = "json" # str | Output format: [JSON|CSV] Json is the default value (optional) if omitted the server will use the default value of "json"
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the lists of indicators.
        api_response = api_instance.economic_data_indicator_list_get(page=page, indicator_name=indicator_name, iso3=iso3, format=format, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling EconomicDataApi->economic_data_indicator_list_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number for paged results | [optional] if omitted the server will use the default value of 1
 **indicator_name** | **str**| Unique indicator name. | [optional] if omitted the server will use the default value of ""
 **iso3** | **str**| The code to identify the country. Must be a ISO-3166 Alpha 3 code. | [optional] if omitted the server will use the default value of ""
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] if omitted the server will use the default value of "json"
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional]

### Return type

[**EconomicIndicatorPropertyPagedResult**](EconomicIndicatorPropertyPagedResult.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **economic_data_indicator_name_get**
> file_type economic_data_indicator_name_get(indicator_name)

Returns the time series of values for different indicators.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  Indicator name as retrieved from /EconomicData/IndicatorList is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import economic_data_api
from data_bridges_client.model.problem_details import ProblemDetails
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
    api_instance = economic_data_api.EconomicDataApi(api_client)
    indicator_name = "indicatorName_example" # str | Name of the indicator as found in /EconomicData/IndicatorList.
    page = 1 # int | Page number for paged results (optional) if omitted the server will use the default value of 1
    iso3 = "" # str | The code to identify the country. Must be a ISO-3166 Alpha 3 code. (optional) if omitted the server will use the default value of ""
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    format = "json" # str | Output format: [JSON|CSV] Json is the default value (optional) if omitted the server will use the default value of "json"
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns the time series of values for different indicators.
        api_response = api_instance.economic_data_indicator_name_get(indicator_name)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling EconomicDataApi->economic_data_indicator_name_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the time series of values for different indicators.
        api_response = api_instance.economic_data_indicator_name_get(indicator_name, page=page, iso3=iso3, start_date=start_date, end_date=end_date, format=format, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling EconomicDataApi->economic_data_indicator_name_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indicator_name** | **str**| Name of the indicator as found in /EconomicData/IndicatorList. |
 **page** | **int**| Page number for paged results | [optional] if omitted the server will use the default value of 1
 **iso3** | **str**| The code to identify the country. Must be a ISO-3166 Alpha 3 code. | [optional] if omitted the server will use the default value of ""
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] if omitted the server will use the default value of "json"
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional]

### Return type

**file_type**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

