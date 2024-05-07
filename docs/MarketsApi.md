# data_bridges_client.MarketsApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**markets_geo_json_list_get**](MarketsApi.md#markets_geo_json_list_get) | **GET** /Markets/GeoJSONList | Provide a list of geo referenced markets in a specific country
[**markets_list_get**](MarketsApi.md#markets_list_get) | **GET** /Markets/List | Get a complete list of markets in a country
[**markets_markets_as_csv_get**](MarketsApi.md#markets_markets_as_csv_get) | **GET** /Markets/MarketsAsCSV | Get a complete list of markets in a country
[**markets_nearby_markets_get**](MarketsApi.md#markets_nearby_markets_get) | **GET** /Markets/NearbyMarkets | Find markets near a given location by longitude and latitude within a 15Km distance


# **markets_geo_json_list_get**
> MarketGeoJsonRoot markets_geo_json_list_get(adm0code=adm0code, env=env)

Provide a list of geo referenced markets in a specific country

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_markets-geojsonlist_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.market_geo_json_root import MarketGeoJsonRoot
from data_bridges_client.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.MarketsApi(api_client)
    adm0code = 56 # int | The admin code of the country (optional)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Provide a list of geo referenced markets in a specific country
        api_response = api_instance.markets_geo_json_list_get(adm0code=adm0code, env=env)
        print("The response of MarketsApi->markets_geo_json_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketsApi->markets_geo_json_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm0code** | **int**| The admin code of the country | [optional] 
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**MarketGeoJsonRoot**](MarketGeoJsonRoot.md)

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
> PagedMarketListDTO markets_list_get(country_code=country_code, page=page, format=format, env=env)

Get a complete list of markets in a country

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_markets-list_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_market_list_dto import PagedMarketListDTO
from data_bridges_client.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.MarketsApi(api_client)
    country_code = 'country_code_example' # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code (optional)
    page = 1 # int | page number for paged results (optional) (default to 1)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Get a complete list of markets in a country
        api_response = api_instance.markets_list_get(country_code=country_code, page=page, format=format, env=env)
        print("The response of MarketsApi->markets_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketsApi->markets_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code | [optional] 
 **page** | **int**| page number for paged results | [optional] [default to 1]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**PagedMarketListDTO**](PagedMarketListDTO.md)

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
> bytearray markets_markets_as_csv_get(adm0code=adm0code, local_names=local_names, env=env)

Get a complete list of markets in a country

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_markets-marketsascsv_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.MarketsApi(api_client)
    adm0code = 56 # int | The admin code of the country (optional)
    local_names = False # bool | If true the name of markets and regions will be localized if available (optional) (default to False)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Get a complete list of markets in a country
        api_response = api_instance.markets_markets_as_csv_get(adm0code=adm0code, local_names=local_names, env=env)
        print("The response of MarketsApi->markets_markets_as_csv_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketsApi->markets_markets_as_csv_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm0code** | **int**| The admin code of the country | [optional] 
 **local_names** | **bool**| If true the name of markets and regions will be localized if available | [optional] [default to False]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

**bytearray**

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
> List[NearbyMarketsDTO] markets_nearby_markets_get(adm0code=adm0code, lat=lat, lng=lng, env=env)

Find markets near a given location by longitude and latitude within a 15Km distance

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_markets-nearbymarkets_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.nearby_markets_dto import NearbyMarketsDTO
from data_bridges_client.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.MarketsApi(api_client)
    adm0code = 56 # int | code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion (optional)
    lat = 3.4 # float | latitude of the point that will be used to search for existing nearby markets. Geo-reference standard used for this coordinate is decimal (optional)
    lng = 3.4 # float | longitude of the point that will be used to search for existing nearby markets.  Geo-reference standard used for this coordinate is decimal (optional)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Find markets near a given location by longitude and latitude within a 15Km distance
        api_response = api_instance.markets_nearby_markets_get(adm0code=adm0code, lat=lat, lng=lng, env=env)
        print("The response of MarketsApi->markets_nearby_markets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarketsApi->markets_nearby_markets_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm0code** | **int**| code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion | [optional] 
 **lat** | **float**| latitude of the point that will be used to search for existing nearby markets. Geo-reference standard used for this coordinate is decimal | [optional] 
 **lng** | **float**| longitude of the point that will be used to search for existing nearby markets.  Geo-reference standard used for this coordinate is decimal | [optional] 
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**List[NearbyMarketsDTO]**](NearbyMarketsDTO.md)

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

