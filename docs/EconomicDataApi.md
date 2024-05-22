# data_bridges_client.EconomicDataApi

<<<<<<< HEAD
All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.1.0*
=======
All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.0.0*
>>>>>>> dev

Method | HTTP request | Description
------------- | ------------- | -------------
[**economic_data_indicator_list_get**](EconomicDataApi.md#economic_data_indicator_list_get) | **GET** /EconomicData/IndicatorList | Returns the lists of indicators.
[**economic_data_indicator_name_get**](EconomicDataApi.md#economic_data_indicator_name_get) | **GET** /EconomicData/{indicatorName} | Returns the time series of values for different indicators.


# **economic_data_indicator_list_get**
> EconomicIndicatorPropertyPagedResult economic_data_indicator_list_get(page=page, indicator_name=indicator_name, iso3=iso3, format=format, env=env)

Returns the lists of indicators.

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_economicdata-indicatorlist_get\"  Returns the lists of indicators for which Vulnerability Analysis and Mapping - Economic and Market Analysis Unit has redistribution licensing from Trading Economics. No mandatory parameter.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_economicdata-indicatorlist_get\"  Returns the lists of indicators for which Vulnerability Analysis and Mapping - Economic and Market Analysis Unit has redistribution licensing from Trading Economics. No mandatory parameter.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.economic_indicator_property_paged_result import EconomicIndicatorPropertyPagedResult
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
    api_instance = data_bridges_client.EconomicDataApi(api_client)
    page = 1 # int | Page number for paged results (optional) (default to 1)
    indicator_name = '' # str | Unique indicator name. (optional) (default to '')
    iso3 = '' # str | The code to identify the country. Must be a ISO-3166 Alpha 3 code. (optional) (default to '')
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Returns the lists of indicators.
        api_response = api_instance.economic_data_indicator_list_get(page=page, indicator_name=indicator_name, iso3=iso3, format=format, env=env)
        print("The response of EconomicDataApi->economic_data_indicator_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomicDataApi->economic_data_indicator_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number for paged results | [optional] [default to 1]
 **indicator_name** | **str**| Unique indicator name. | [optional] [default to &#39;&#39;]
 **iso3** | **str**| The code to identify the country. Must be a ISO-3166 Alpha 3 code. | [optional] [default to &#39;&#39;]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**EconomicIndicatorPropertyPagedResult**](EconomicIndicatorPropertyPagedResult.md)

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

# **economic_data_indicator_name_get**
> PagedEconomicDataDTO economic_data_indicator_name_get(indicator_name, page=page, iso3=iso3, start_date=start_date, end_date=end_date, format=format, env=env)

Returns the time series of values for different indicators.

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_economicdata_get\"  Indicator name as retrieved from /EconomicData/IndicatorList is mandatory.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_economicdata_get\"  Indicator name as retrieved from /EconomicData/IndicatorList is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_economic_data_dto import PagedEconomicDataDTO
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
    api_instance = data_bridges_client.EconomicDataApi(api_client)
    indicator_name = 'indicator_name_example' # str | Name of the indicator as found in /EconomicData/IndicatorList.
    page = 1 # int | Page number for paged results (optional) (default to 1)
    iso3 = '' # str | The code to identify the country. Must be a ISO-3166 Alpha 3 code. (optional) (default to '')
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24) (optional)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Returns the time series of values for different indicators.
        api_response = api_instance.economic_data_indicator_name_get(indicator_name, page=page, iso3=iso3, start_date=start_date, end_date=end_date, format=format, env=env)
        print("The response of EconomicDataApi->economic_data_indicator_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EconomicDataApi->economic_data_indicator_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indicator_name** | **str**| Name of the indicator as found in /EconomicData/IndicatorList. | 
 **page** | **int**| Page number for paged results | [optional] [default to 1]
 **iso3** | **str**| The code to identify the country. Must be a ISO-3166 Alpha 3 code. | [optional] [default to &#39;&#39;]
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\&quot;-\\\&quot; month \\\&quot;-\\\&quot; day (e.g. 2020/06/24) | [optional] 
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**PagedEconomicDataDTO**](PagedEconomicDataDTO.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

