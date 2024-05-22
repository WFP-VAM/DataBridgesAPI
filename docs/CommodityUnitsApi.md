# data_bridges_client.CommodityUnitsApi

<<<<<<< HEAD
All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.1.0*
=======
All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.0.0*
>>>>>>> dev

Method | HTTP request | Description
------------- | ------------- | -------------
[**commodity_units_conversion_list_get**](CommodityUnitsApi.md#commodity_units_conversion_list_get) | **GET** /CommodityUnits/Conversion/List | Provides conversion factors to Kilogram or Litres for each convertible unit of measure.
[**commodity_units_list_get**](CommodityUnitsApi.md#commodity_units_list_get) | **GET** /CommodityUnits/List | Provides the detailed list of the unit of measure available in DataBridges platform


# **commodity_units_conversion_list_get**
> PagedCommodityListDTO commodity_units_conversion_list_get(country_code=country_code, commodity_id=commodity_id, from_unit_id=from_unit_id, to_unit_id=to_unit_id, page=page, format=format, env=env)

Provides conversion factors to Kilogram or Litres for each convertible unit of measure.

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_commodityunits-conversion-list_get\"  Some non-standard units of measure might have different a conversion factor based on the country [Adm0Code]; Other non-standard units of measure might have a different conversion factor based on the commodity [CommodityID] being measured. Other cases will have null adm0code and CommodityID. No mandatory parameter.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_commodityunits-conversion-list_get\"  Some non-standard units of measure might have different a conversion factor based on the country [Adm0Code]; Other non-standard units of measure might have a different conversion factor based on the commodity [CommodityID] being measured. Other cases will have null adm0code and CommodityID. No mandatory parameter.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_commodity_list_dto import PagedCommodityListDTO
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
    api_instance = data_bridges_client.CommodityUnitsApi(api_client)
    country_code = 'country_code_example' # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    commodity_id = 0 # int | The exact ID of a Commodity, as found in /Commodities/List (optional) (default to 0)
    from_unit_id = 0 # int | The exact ID of the original unit of measure of the price of a commodity, as found in /CommodityUnits/List (optional) (default to 0)
    to_unit_id = 0 # int | The exact ID of the converted unit of measure of the price of a commodity, as found in /CommodityUnits/List (optional) (default to 0)
    page = 1 # int | Page number for paged results (optional) (default to 1)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Provides conversion factors to Kilogram or Litres for each convertible unit of measure.
        api_response = api_instance.commodity_units_conversion_list_get(country_code=country_code, commodity_id=commodity_id, from_unit_id=from_unit_id, to_unit_id=to_unit_id, page=page, format=format, env=env)
        print("The response of CommodityUnitsApi->commodity_units_conversion_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommodityUnitsApi->commodity_units_conversion_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional] 
 **commodity_id** | **int**| The exact ID of a Commodity, as found in /Commodities/List | [optional] [default to 0]
 **from_unit_id** | **int**| The exact ID of the original unit of measure of the price of a commodity, as found in /CommodityUnits/List | [optional] [default to 0]
 **to_unit_id** | **int**| The exact ID of the converted unit of measure of the price of a commodity, as found in /CommodityUnits/List | [optional] [default to 0]
 **page** | **int**| Page number for paged results | [optional] [default to 1]
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
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **commodity_units_list_get**
> PagedCommodityListDTO commodity_units_list_get(country_code=country_code, commodity_unit_name=commodity_unit_name, commodity_unit_id=commodity_unit_id, page=page, format=format, env=env)

Provides the detailed list of the unit of measure available in DataBridges platform

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_commodityunits-list_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_commodityunits-list_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_commodity_list_dto import PagedCommodityListDTO
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
    api_instance = data_bridges_client.CommodityUnitsApi(api_client)
    country_code = 'country_code_example' # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code (optional)
    commodity_unit_name = 'commodity_unit_name_example' # str | The name, even partial and case insensitive, of a commodity unit (optional)
    commodity_unit_id = 0 # int | The exact ID of a commodity unit (optional) (default to 0)
    page = 1 # int | page number for paged results (optional) (default to 1)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Provides the detailed list of the unit of measure available in DataBridges platform
        api_response = api_instance.commodity_units_list_get(country_code=country_code, commodity_unit_name=commodity_unit_name, commodity_unit_id=commodity_unit_id, page=page, format=format, env=env)
        print("The response of CommodityUnitsApi->commodity_units_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommodityUnitsApi->commodity_units_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code | [optional] 
 **commodity_unit_name** | **str**| The name, even partial and case insensitive, of a commodity unit | [optional] 
 **commodity_unit_id** | **int**| The exact ID of a commodity unit | [optional] [default to 0]
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
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

