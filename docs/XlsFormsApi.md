# data_bridges_client.XlsFormsApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/1.3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**m_fi_xls_forms_definition_get**](XlsFormsApi.md#m_fi_xls_forms_definition_get) | **GET** /MFI/XlsForms/definition | Get a complete set of XLS Form definitions of a given XLS Form ID. This is the digital version of the questionnaire used during the data collection exercise.
[**m_fi_xls_forms_get**](XlsFormsApi.md#m_fi_xls_forms_get) | **GET** /MFI/XlsForms | Get a complete list of XLS Forms uploaded on the MFI Data Bridge in a given period of data collection. This is the digital version of the questionnaire used during the data collection exercise.


# **m_fi_xls_forms_definition_get**
> [XlsFormDefinitionDTO] m_fi_xls_forms_definition_get()

Get a complete set of XLS Form definitions of a given XLS Form ID. This is the digital version of the questionnaire used during the data collection exercise.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import xls_forms_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.xls_form_definition_dto import XlsFormDefinitionDTO
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
    api_instance = xls_forms_api.XlsFormsApi(api_client)
    xls_form_id = 1 # int | unique identifier for the XLS Form, as retrieved from /XLSForms (optional)
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a complete set of XLS Form definitions of a given XLS Form ID. This is the digital version of the questionnaire used during the data collection exercise.
        api_response = api_instance.m_fi_xls_forms_definition_get(xls_form_id=xls_form_id, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling XlsFormsApi->m_fi_xls_forms_definition_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xls_form_id** | **int**| unique identifier for the XLS Form, as retrieved from /XLSForms | [optional]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional]

### Return type

[**[XlsFormDefinitionDTO]**](XlsFormDefinitionDTO.md)

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

# **m_fi_xls_forms_get**
> [PagedXlsFormListDTO] m_fi_xls_forms_get()

Get a complete list of XLS Forms uploaded on the MFI Data Bridge in a given period of data collection. This is the digital version of the questionnaire used during the data collection exercise.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import xls_forms_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.paged_xls_form_list_dto import PagedXlsFormListDTO
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
    api_instance = xls_forms_api.XlsFormsApi(api_client)
    adm0_code = 0 # int | code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion (optional) if omitted the server will use the default value of 0
    page = 1 # int | page number for paged results (optional) if omitted the server will use the default value of 1
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | starting date for the range in which data using this XLSForm was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ending date for the range in which data using this XLSForm was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a complete list of XLS Forms uploaded on the MFI Data Bridge in a given period of data collection. This is the digital version of the questionnaire used during the data collection exercise.
        api_response = api_instance.m_fi_xls_forms_get(adm0_code=adm0_code, page=page, start_date=start_date, end_date=end_date, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling XlsFormsApi->m_fi_xls_forms_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm0_code** | **int**| code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion | [optional] if omitted the server will use the default value of 0
 **page** | **int**| page number for paged results | [optional] if omitted the server will use the default value of 1
 **start_date** | **datetime**| starting date for the range in which data using this XLSForm was collected. Use the date formats defined by RFC 3339 ; use strings matching year \&quot;-\&quot; month \&quot;-\&quot; day (e.g. 2020/06/24) | [optional]
 **end_date** | **datetime**| ending date for the range in which data using this XLSForm was collected. Use the date formats defined by RFC 3339 ; use strings matching year \&quot;-\&quot; month \&quot;-\&quot; day (e.g. 2020/06/24) | [optional]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional]

### Return type

[**[PagedXlsFormListDTO]**](PagedXlsFormListDTO.md)

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
