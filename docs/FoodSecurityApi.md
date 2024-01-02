# data_bridges_client.FoodSecurityApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/1.4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**food_security_list_get**](FoodSecurityApi.md#food_security_list_get) | **GET** /FoodSecurity/List | 


# **food_security_list_get**
> IpcValuePagedResult food_security_list_get()



  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import food_security_api
from data_bridges_client.model.ipc_value_paged_result import IpcValuePagedResult
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from pprint import pprint
# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/1.4.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.4.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: default
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/1.4.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = food_security_api.FoodSecurityApi(api_client)
    iso3 = "iso3_example" # str | The country ISO3 code (optional)
    year = 1 # int |  (optional)
    page = 1 # int |  (optional) if omitted the server will use the default value of 1
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.food_security_list_get(iso3=iso3, year=year, page=page, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling FoodSecurityApi->food_security_list_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iso3** | **str**| The country ISO3 code | [optional]
 **year** | **int**|  | [optional]
 **page** | **int**|  | [optional] if omitted the server will use the default value of 1
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - api.vam.wfp.org | [optional]

### Return type

[**IpcValuePagedResult**](IpcValuePagedResult.md)

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

