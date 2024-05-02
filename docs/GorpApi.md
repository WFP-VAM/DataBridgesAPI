# data_bridges_client.GorpApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gorp_latest_get**](GorpApi.md#gorp_latest_get) | **GET** /Gorp/Latest | Return the latest dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.
[**gorp_list_get**](GorpApi.md#gorp_list_get) | **GET** /Gorp/List | Return the full dataset of number of acutely food insecure (in millions) based on WFP Global Operational Response Plan.


# **gorp_latest_get**
> GorpValueWithChangesPagedResult gorp_latest_get()

Return the latest dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_gorp-latest_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import gorp_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.gorp_value_with_changes_paged_result import GorpValueWithChangesPagedResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: default
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.0.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gorp_api.GorpApi(api_client)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return the latest dataset of number of acutely food insecure (in millions)  based on WFP Global Operational Response Plan.
        api_response = api_instance.gorp_latest_get(page=page, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling GorpApi->gorp_latest_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
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
> GorpValueWithChangesPagedResult gorp_list_get()

Return the full dataset of number of acutely food insecure (in millions) based on WFP Global Operational Response Plan.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_gorp-list_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import gorp_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.gorp_value_with_changes_paged_result import GorpValueWithChangesPagedResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: default
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.0.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gorp_api.GorpApi(api_client)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return the full dataset of number of acutely food insecure (in millions) based on WFP Global Operational Response Plan.
        api_response = api_instance.gorp_list_get(page=page, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling GorpApi->gorp_list_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
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

