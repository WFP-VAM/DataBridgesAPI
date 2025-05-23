# data_bridges_client.CommoditiesApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/6.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commodities_categories_list_get**](CommoditiesApi.md#commodities_categories_list_get) | **GET** /Commodities/Categories/List | Provides the list of categories.
[**commodities_list_get**](CommoditiesApi.md#commodities_list_get) | **GET** /Commodities/List | Provide the detailed list of the commodities available in DataBridges platform


# **commodities_categories_list_get**
> PagedCommodityListDTO commodities_categories_list_get(country_code=country_code, category_name=category_name, category_id=category_id, page=page, format=format, env=env)

Provides the list of categories.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_commodities-categories-list_get\"  Categories are matched with high level WFP commodity classification at level 1. No mandatory parameter.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_commodity_list_dto import PagedCommodityListDTO
from data_bridges_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/6.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/6.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

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
    except Exception as e:
        print("Exception when calling CommoditiesApi->commodities_categories_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code | [optional] 
 **category_name** | **str**| The name, even partial and case insensitive, of a commodity category. | [optional] 
 **category_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List. | [optional] [default to 0]
 **page** | **int**| page number for paged results | [optional] [default to 1]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**PagedCommodityListDTO**](PagedCommodityListDTO.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commodities_list_get**
> PagedCommodityListDTO commodities_list_get(country_code=country_code, commodity_name=commodity_name, commodity_id=commodity_id, page=page, format=format, env=env)

Provide the detailed list of the commodities available in DataBridges platform

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_commodities-list_get\"  COICOP 2018 codes are returned to hierarchically matching categories based on [UN-Statistical Division codes](https://unstats.un.org/unsd/classifications/Econ/). No mandatory parameter.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_commodity_list_dto import PagedCommodityListDTO
from data_bridges_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/6.0.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/6.0.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.CommoditiesApi(api_client)
    country_code = 'country_code_example' # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code (optional)
    commodity_name = 'commodity_name_example' # str | The name, even partial and case insensitive, of a commodity (optional)
    commodity_id = 0 # int | The exact ID of a commodity (optional) (default to 0)
    page = 1 # int | page number for paged results (optional) (default to 1)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Provide the detailed list of the commodities available in DataBridges platform
        api_response = api_instance.commodities_list_get(country_code=country_code, commodity_name=commodity_name, commodity_id=commodity_id, page=page, format=format, env=env)
        print("The response of CommoditiesApi->commodities_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommoditiesApi->commodities_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code | [optional] 
 **commodity_name** | **str**| The name, even partial and case insensitive, of a commodity | [optional] 
 **commodity_id** | **int**| The exact ID of a commodity | [optional] [default to 0]
 **page** | **int**| page number for paged results | [optional] [default to 1]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**PagedCommodityListDTO**](PagedCommodityListDTO.md)

### Authorization

[default](../README.md#default)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

