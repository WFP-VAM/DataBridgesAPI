# data_bridges_client.MarketsApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/1.4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**markets_geo_json_list_get**](MarketsApi.md#markets_geo_json_list_get) | **GET** /Markets/GeoJSONList | Provide a list of geo referenced markets in a specific country
[**markets_list_get**](MarketsApi.md#markets_list_get) | **GET** /Markets/List | Get a complete list of markets in a country
[**markets_markets_as_csv_get**](MarketsApi.md#markets_markets_as_csv_get) | **GET** /Markets/MarketsAsCSV | Get a complete list of markets in a country
[**markets_nearby_markets_get**](MarketsApi.md#markets_nearby_markets_get) | **GET** /Markets/NearbyMarkets | Find markets near a given location by longitude and latitude within a 15Km distance


# **markets_geo_json_list_get**
> [IFeature] markets_geo_json_list_get()

Provide a list of geo referenced markets in a specific country

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import markets_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.i_feature import IFeature
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
    api_instance = markets_api.MarketsApi(api_client)
    adm0code = 1 # int | The admin code of the country (optional)
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Provide a list of geo referenced markets in a specific country
        api_response = api_instance.markets_geo_json_list_get(adm0code=adm0code, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling MarketsApi->markets_geo_json_list_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm0code** | **int**| The admin code of the country | [optional]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - api.vam.wfp.org | [optional]

### Return type

[**[IFeature]**](IFeature.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets_list_get**
> file_type markets_list_get()

Get a complete list of markets in a country

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import markets_api
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
    api_instance = markets_api.MarketsApi(api_client)
    country_code = "countryCode_example" # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code (optional)
    page = 1 # int | page number for paged results (optional) if omitted the server will use the default value of 1
    format = "json" # str | Output format: [JSON|CSV] Json is the default value (optional) if omitted the server will use the default value of "json"
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a complete list of markets in a country
        api_response = api_instance.markets_list_get(country_code=country_code, page=page, format=format, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling MarketsApi->markets_list_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code | [optional]
 **page** | **int**| page number for paged results | [optional] if omitted the server will use the default value of 1
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] if omitted the server will use the default value of "json"
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - api.vam.wfp.org | [optional]

### Return type

**file_type**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets_markets_as_csv_get**
> file_type markets_markets_as_csv_get()

Get a complete list of markets in a country

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import markets_api
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
    api_instance = markets_api.MarketsApi(api_client)
    adm0code = 1 # int | The admin code of the country (optional)
    local_names = False # bool | If true the name of markets and regions will be localized if available (optional) if omitted the server will use the default value of False
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a complete list of markets in a country
        api_response = api_instance.markets_markets_as_csv_get(adm0code=adm0code, local_names=local_names, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling MarketsApi->markets_markets_as_csv_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm0code** | **int**| The admin code of the country | [optional]
 **local_names** | **bool**| If true the name of markets and regions will be localized if available | [optional] if omitted the server will use the default value of False
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - api.vam.wfp.org | [optional]

### Return type

**file_type**

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markets_nearby_markets_get**
> [NearbyMarketsDTO] markets_nearby_markets_get()

Find markets near a given location by longitude and latitude within a 15Km distance

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import markets_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.nearby_markets_dto import NearbyMarketsDTO
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
    api_instance = markets_api.MarketsApi(api_client)
    adm0code = 1 # int | code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion (optional)
    lat = 3.14 # float | latitude of the point that will be used to search for existing nearby markets. Geo-reference standard used for this coordinate is decimal (optional)
    lng = 3.14 # float | longitude of the point that will be used to search for existing nearby markets.  Geo-reference standard used for this coordinate is decimal (optional)
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find markets near a given location by longitude and latitude within a 15Km distance
        api_response = api_instance.markets_nearby_markets_get(adm0code=adm0code, lat=lat, lng=lng, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling MarketsApi->markets_nearby_markets_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm0code** | **int**| code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion | [optional]
 **lat** | **float**| latitude of the point that will be used to search for existing nearby markets. Geo-reference standard used for this coordinate is decimal | [optional]
 **lng** | **float**| longitude of the point that will be used to search for existing nearby markets.  Geo-reference standard used for this coordinate is decimal | [optional]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - api.vam.wfp.org | [optional]

### Return type

[**[NearbyMarketsDTO]**](NearbyMarketsDTO.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

