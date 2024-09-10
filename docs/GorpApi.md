# data_bridges_client.GorpApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/5.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gorp_country_latest_get**](GorpApi.md#gorp_country_latest_get) | **GET** /Gorp/CountryLatest | Return the latest country dataset of number of acutely food insecure (in thousands)  based on WFP Global Operational Response Plan.
[**gorp_global_latest_get**](GorpApi.md#gorp_global_latest_get) | **GET** /Gorp/GlobalLatest | Return the latest global dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.
[**gorp_latest_get**](GorpApi.md#gorp_latest_get) | **GET** /Gorp/Latest | Return the latest dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.
[**gorp_list_get**](GorpApi.md#gorp_list_get) | **GET** /Gorp/List | Return the full dataset of number of acutely food insecure (in millions) based on WFP Global Operational Response Plan.
[**gorp_regional_latest_get**](GorpApi.md#gorp_regional_latest_get) | **GET** /Gorp/RegionalLatest | Return the latest regional dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.


# **gorp_country_latest_get**
> List[GorpCountryApiDto] gorp_country_latest_get(env=env)

Return the latest country dataset of number of acutely food insecure (in thousands)  based on WFP Global Operational Response Plan.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_gorp-countrylatest_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.gorp_country_api_dto import GorpCountryApiDto
from data_bridges_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/5.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/5.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.GorpApi(api_client)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Return the latest country dataset of number of acutely food insecure (in thousands)  based on WFP Global Operational Response Plan.
        api_response = api_instance.gorp_country_latest_get(env=env)
        print("The response of GorpApi->gorp_country_latest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GorpApi->gorp_country_latest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**List[GorpCountryApiDto]**](GorpCountryApiDto.md)

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

# **gorp_global_latest_get**
> GorpGlobalApiDto gorp_global_latest_get(env=env)

Return the latest global dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_gorp-globallatest_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.gorp_global_api_dto import GorpGlobalApiDto
from data_bridges_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/5.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/5.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.GorpApi(api_client)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Return the latest global dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.
        api_response = api_instance.gorp_global_latest_get(env=env)
        print("The response of GorpApi->gorp_global_latest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GorpApi->gorp_global_latest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**GorpGlobalApiDto**](GorpGlobalApiDto.md)

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

# **gorp_latest_get**
> GorpValueWithChangesPagedResult gorp_latest_get(page=page, env=env)

Return the latest dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_gorp-latest_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.gorp_value_with_changes_paged_result import GorpValueWithChangesPagedResult
from data_bridges_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/5.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/5.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.GorpApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Return the latest dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.
        api_response = api_instance.gorp_latest_get(page=page, env=env)
        print("The response of GorpApi->gorp_latest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GorpApi->gorp_latest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**GorpValueWithChangesPagedResult**](GorpValueWithChangesPagedResult.md)

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

# **gorp_list_get**
> GorpValueWithChangesPagedResult gorp_list_get(page=page, env=env)

Return the full dataset of number of acutely food insecure (in millions) based on WFP Global Operational Response Plan.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_gorp-list_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.gorp_value_with_changes_paged_result import GorpValueWithChangesPagedResult
from data_bridges_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/5.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/5.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.GorpApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Return the full dataset of number of acutely food insecure (in millions) based on WFP Global Operational Response Plan.
        api_response = api_instance.gorp_list_get(page=page, env=env)
        print("The response of GorpApi->gorp_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GorpApi->gorp_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**GorpValueWithChangesPagedResult**](GorpValueWithChangesPagedResult.md)

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

# **gorp_regional_latest_get**
> List[GorpRegionalApiDto] gorp_regional_latest_get(env=env)

Return the latest regional dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_gorp-regionallatest_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.gorp_regional_api_dto import GorpRegionalApiDto
from data_bridges_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/5.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/5.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.GorpApi(api_client)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Return the latest regional dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.
        api_response = api_instance.gorp_regional_latest_get(env=env)
        print("The response of GorpApi->gorp_regional_latest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GorpApi->gorp_regional_latest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**List[GorpRegionalApiDto]**](GorpRegionalApiDto.md)

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

