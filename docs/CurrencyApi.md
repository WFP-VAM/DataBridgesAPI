# data_bridges_client.CurrencyApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currency_list_get**](CurrencyApi.md#currency_list_get) | **GET** /Currency/List | Returns the list of currencies available in the internal VAM database, with Currency 3-letter code, matching with ISO 4217.
[**currency_usd_indirect_quotation_get**](CurrencyApi.md#currency_usd_indirect_quotation_get) | **GET** /Currency/UsdIndirectQuotation | Returns the value of the Exchange rates from Trading Economics, for official rates, and DataViz for unofficial rates.


# **currency_list_get**
> PagedCurrencyListDTO currency_list_get()

Returns the list of currencies available in the internal VAM database, with Currency 3-letter code, matching with ISO 4217.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_currency-list_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import currency_api
from data_bridges_client.model.paged_currency_list_dto import PagedCurrencyListDTO
from data_bridges_client.model.bad_request_dto import BadRequestDTO
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
    api_instance = currency_api.CurrencyApi(api_client)
    country_code = "countryCode_example" # str | The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. (optional)
    currency_name = "currencyName_example" # str | Currency 3-letter code, matching with ISO 4217. (optional)
    currency_id = 0 # int | Unique code to identify the currency in internal VAM currencies. (optional) if omitted the server will use the default value of 0
    page = 1 # int | Page number for paged results (optional) if omitted the server will use the default value of 1
    format = "json" # str | Output format: [JSON|CSV] Json is the default value (optional) if omitted the server will use the default value of "json"
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the list of currencies available in the internal VAM database, with Currency 3-letter code, matching with ISO 4217.
        api_response = api_instance.currency_list_get(country_code=country_code, currency_name=currency_name, currency_id=currency_id, page=page, format=format, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling CurrencyApi->currency_list_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. | [optional]
 **currency_name** | **str**| Currency 3-letter code, matching with ISO 4217. | [optional]
 **currency_id** | **int**| Unique code to identify the currency in internal VAM currencies. | [optional] if omitted the server will use the default value of 0
 **page** | **int**| Page number for paged results | [optional] if omitted the server will use the default value of 1
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] if omitted the server will use the default value of "json"
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional]

### Return type

[**PagedCurrencyListDTO**](PagedCurrencyListDTO.md)

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

# **currency_usd_indirect_quotation_get**
> UsdIndirectQuotationPagedResult currency_usd_indirect_quotation_get()

Returns the value of the Exchange rates from Trading Economics, for official rates, and DataViz for unofficial rates.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_currency-usdindirectquotation_get\"  Returns the time series of values of the Exchange rate of the Local Currency for buying 1 USD in the official market. Original frequency for official rates is daily, non-indicated. Unofficial rates are aggregated at national level by the original frequency of collection. For greater detail on unofficial exchange rates, explore the Exchange Rate (unofficial) commodity in Market Prices Prices. No mandatory parameter.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import currency_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.usd_indirect_quotation_paged_result import UsdIndirectQuotationPagedResult
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
    api_instance = currency_api.CurrencyApi(api_client)
    country_iso3 = "" # str | The code to identify the country. Must be a ISO-3166 Alpha 3 code. (optional) if omitted the server will use the default value of ""
    currency_name = "" # str | the ISO3 code for the currency, based on ISO4217 (optional) if omitted the server will use the default value of ""
    page = 1 # int | Page number for paged results (optional) if omitted the server will use the default value of 1
    format = "json" # str | Output format: [JSON|CSV] Json is the default value (optional) if omitted the server will use the default value of "json"
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns the value of the Exchange rates from Trading Economics, for official rates, and DataViz for unofficial rates.
        api_response = api_instance.currency_usd_indirect_quotation_get(country_iso3=country_iso3, currency_name=currency_name, page=page, format=format, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling CurrencyApi->currency_usd_indirect_quotation_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_iso3** | **str**| The code to identify the country. Must be a ISO-3166 Alpha 3 code. | [optional] if omitted the server will use the default value of ""
 **currency_name** | **str**| the ISO3 code for the currency, based on ISO4217 | [optional] if omitted the server will use the default value of ""
 **page** | **int**| Page number for paged results | [optional] if omitted the server will use the default value of 1
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] if omitted the server will use the default value of "json"
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional]

### Return type

[**UsdIndirectQuotationPagedResult**](UsdIndirectQuotationPagedResult.md)

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

