# data_bridges_client.RpmeApi

<<<<<<< HEAD
All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.1.0*
=======
All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.0.0*
>>>>>>> dev

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpme_base_data_get**](RpmeApi.md#rpme_base_data_get) | **GET** /Rpme/BaseData | Get data that includes the core RPME fields only by Survey ID
[**rpme_full_data_get**](RpmeApi.md#rpme_full_data_get) | **GET** /Rpme/FullData | Get a full dataset that includes all the fields included in the survey in addition to the core RPME fields by Survey ID.
[**rpme_output_values_get**](RpmeApi.md#rpme_output_values_get) | **GET** /Rpme/OutputValues | Processed values for each variable used in the assessments
[**rpme_surveys_get**](RpmeApi.md#rpme_surveys_get) | **GET** /Rpme/Surveys | Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all RPME surveys conducted in a country. The date of reference, SurveyDate, for the data collection is set by the officer responsible for the upload of each survey.
[**rpme_variables_get**](RpmeApi.md#rpme_variables_get) | **GET** /Rpme/Variables | List of variables
[**rpme_xls_forms_get**](RpmeApi.md#rpme_xls_forms_get) | **GET** /Rpme/XLSForms | Get a complete list of XLS Forms uploaded on the RPME in a given period of data collection. This is the digital version of the questionnaire used during the data collection exercise.


# **rpme_base_data_get**
> PagedSurveyResponsesDTO rpme_base_data_get(survey_id=survey_id, page=page, page_size=page_size, env=env)

Get data that includes the core RPME fields only by Survey ID

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-basedata_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-basedata_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_survey_responses_dto import PagedSurveyResponsesDTO
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
    api_instance = data_bridges_client.RpmeApi(api_client)
    survey_id = 56 # int | unique identifier for the collected data, as retrieved from /Surveys API. (optional)
    page = 1 # int | page number for paged results (optional) (default to 1)
    page_size = 20 # int | page size for paged results, default value is 20. (optional) (default to 20)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Get data that includes the core RPME fields only by Survey ID
        api_response = api_instance.rpme_base_data_get(survey_id=survey_id, page=page, page_size=page_size, env=env)
        print("The response of RpmeApi->rpme_base_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpmeApi->rpme_base_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| unique identifier for the collected data, as retrieved from /Surveys API. | [optional] 
 **page** | **int**| page number for paged results | [optional] [default to 1]
 **page_size** | **int**| page size for paged results, default value is 20. | [optional] [default to 20]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**PagedSurveyResponsesDTO**](PagedSurveyResponsesDTO.md)

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

# **rpme_full_data_get**
> PagedSurveyResponsesDTO rpme_full_data_get(survey_id=survey_id, format=format, page=page, page_size=page_size, env=env)

Get a full dataset that includes all the fields included in the survey in addition to the core RPME fields by Survey ID.

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-TEC_Architecture_+_Service_Owner_approvals_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Official%20Use%20Only-yellow)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-fulldata_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Restricted-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Official%20Use%20Only-yellow)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-fulldata_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_survey_responses_dto import PagedSurveyResponsesDTO
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
    api_instance = data_bridges_client.RpmeApi(api_client)
    survey_id = 56 # int | unique identifier for the collected data, as retrieved from /Surveys API. (optional)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    page = 1 # int | page number for paged results (optional) (default to 1)
    page_size = 20 # int | page size for paged results, default value is 20. (optional) (default to 20)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Get a full dataset that includes all the fields included in the survey in addition to the core RPME fields by Survey ID.
        api_response = api_instance.rpme_full_data_get(survey_id=survey_id, format=format, page=page, page_size=page_size, env=env)
        print("The response of RpmeApi->rpme_full_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpmeApi->rpme_full_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| unique identifier for the collected data, as retrieved from /Surveys API. | [optional] 
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **page** | **int**| page number for paged results | [optional] [default to 1]
 **page_size** | **int**| page size for paged results, default value is 20. | [optional] [default to 20]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**PagedSurveyResponsesDTO**](PagedSurveyResponsesDTO.md)

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

# **rpme_output_values_get**
> RpmeAssessmentPagedResult rpme_output_values_get(page=page, adm0_code=adm0_code, survey_id=survey_id, shop_id=shop_id, market_id=market_id, adm0_code_dots=adm0_code_dots, env=env)

Processed values for each variable used in the assessments

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-outputvalues_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-outputvalues_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.rpme_assessment_paged_result import RpmeAssessmentPagedResult
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
    api_instance = data_bridges_client.RpmeApi(api_client)
    page = 1 # int | page number for paged results (optional) (default to 1)
    adm0_code = 56 # int | Code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion (optional)
    survey_id = 56 # int | The ID of the survey (optional)
    shop_id = 56 # int | The ID of the shop (optional)
    market_id = 56 # int | The ID of the market (optional)
    adm0_code_dots = '' # str |  (optional) (default to '')
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Processed values for each variable used in the assessments
        api_response = api_instance.rpme_output_values_get(page=page, adm0_code=adm0_code, survey_id=survey_id, shop_id=shop_id, market_id=market_id, adm0_code_dots=adm0_code_dots, env=env)
        print("The response of RpmeApi->rpme_output_values_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpmeApi->rpme_output_values_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number for paged results | [optional] [default to 1]
 **adm0_code** | **int**| Code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion | [optional] 
 **survey_id** | **int**| The ID of the survey | [optional] 
 **shop_id** | **int**| The ID of the shop | [optional] 
 **market_id** | **int**| The ID of the market | [optional] 
 **adm0_code_dots** | **str**|  | [optional] [default to &#39;&#39;]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**RpmeAssessmentPagedResult**](RpmeAssessmentPagedResult.md)

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

# **rpme_surveys_get**
> PagedSurveyListDTO rpme_surveys_get(adm0_code=adm0_code, page=page, start_date=start_date, end_date=end_date, env=env)

Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all RPME surveys conducted in a country. The date of reference, SurveyDate, for the data collection is set by the officer responsible for the upload of each survey.

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-surveys_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-surveys_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_survey_list_dto import PagedSurveyListDTO
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
    api_instance = data_bridges_client.RpmeApi(api_client)
    adm0_code = 0 # int | code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion (optional) (default to 0)
    page = 1 # int | page number for paged results (optional) (default to 1)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all RPME surveys conducted in a country. The date of reference, SurveyDate, for the data collection is set by the officer responsible for the upload of each survey.
        api_response = api_instance.rpme_surveys_get(adm0_code=adm0_code, page=page, start_date=start_date, end_date=end_date, env=env)
        print("The response of RpmeApi->rpme_surveys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpmeApi->rpme_surveys_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm0_code** | **int**| code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion | [optional] [default to 0]
 **page** | **int**| page number for paged results | [optional] [default to 1]
 **start_date** | **datetime**| starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \&quot;-\&quot; month \&quot;-\&quot; day (e.g. 2020/06/24) | [optional] 
 **end_date** | **datetime**| ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \&quot;-\&quot; month \&quot;-\&quot; day (e.g. 2020/06/24) | [optional] 
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**PagedSurveyListDTO**](PagedSurveyListDTO.md)

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

# **rpme_variables_get**
> RpmeVariablePagedResult rpme_variables_get(page=page, env=env)

List of variables

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-variables_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-variables_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.rpme_variable_paged_result import RpmeVariablePagedResult
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
    api_instance = data_bridges_client.RpmeApi(api_client)
    page = 1 # int |  (optional) (default to 1)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # List of variables
        api_response = api_instance.rpme_variables_get(page=page, env=env)
        print("The response of RpmeApi->rpme_variables_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpmeApi->rpme_variables_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**RpmeVariablePagedResult**](RpmeVariablePagedResult.md)

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

# **rpme_xls_forms_get**
> PagedXlsFormListDTO rpme_xls_forms_get(adm0_code=adm0_code, page=page, start_date=start_date, end_date=end_date, env=env)

Get a complete list of XLS Forms uploaded on the RPME in a given period of data collection. This is the digital version of the questionnaire used during the data collection exercise.

<<<<<<< HEAD
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-xlsforms_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
=======
  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_rpme-xlsforms_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern
>>>>>>> dev

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_xls_form_list_dto import PagedXlsFormListDTO
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
    api_instance = data_bridges_client.RpmeApi(api_client)
    adm0_code = 0 # int | code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion (optional) (default to 0)
    page = 1 # int | page number for paged results (optional) (default to 1)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | starting date for the range in which data using this XLSForm was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | ending date for the range in which data using this XLSForm was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Get a complete list of XLS Forms uploaded on the RPME in a given period of data collection. This is the digital version of the questionnaire used during the data collection exercise.
        api_response = api_instance.rpme_xls_forms_get(adm0_code=adm0_code, page=page, start_date=start_date, end_date=end_date, env=env)
        print("The response of RpmeApi->rpme_xls_forms_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RpmeApi->rpme_xls_forms_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm0_code** | **int**| code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion | [optional] [default to 0]
 **page** | **int**| page number for paged results | [optional] [default to 1]
 **start_date** | **datetime**| starting date for the range in which data using this XLSForm was collected. Use the date formats defined by RFC 3339 ; use strings matching year \&quot;-\&quot; month \&quot;-\&quot; day (e.g. 2020/06/24) | [optional] 
 **end_date** | **datetime**| ending date for the range in which data using this XLSForm was collected. Use the date formats defined by RFC 3339 ; use strings matching year \&quot;-\&quot; month \&quot;-\&quot; day (e.g. 2020/06/24) | [optional] 
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**PagedXlsFormListDTO**](PagedXlsFormListDTO.md)

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

