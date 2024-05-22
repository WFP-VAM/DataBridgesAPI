# data_bridges_client.SurveysApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/4.1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**m_fi_surveys_base_data_get**](SurveysApi.md#m_fi_surveys_base_data_get) | **GET** /MFI/Surveys/BaseData | Get data that includes the core Market Functionality Index (MFI) fields only by Survey ID
[**m_fi_surveys_full_data_get**](SurveysApi.md#m_fi_surveys_full_data_get) | **GET** /MFI/Surveys/FullData | Get a full dataset that includes all the fields included in the survey in addition to the core Market Functionality Index (MFI) fields by Survey ID. To access this data, please contact global.mfi@wfp.org for authorization.
[**m_fi_surveys_get**](SurveysApi.md#m_fi_surveys_get) | **GET** /MFI/Surveys | Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all MFI surveys conducted in a country.   A date of reference, SurveyDate, for the data collection is set by the officer responsible for the upload for each survey.
[**m_fi_surveys_processed_data_get**](SurveysApi.md#m_fi_surveys_processed_data_get) | **GET** /MFI/Surveys/ProcessedData | Get a MFI processed data in long format; levels indicate the data aggregation level 1) Normalized Score, 2) Trader Aggregate Score,   3) Market Aggregate Score, 4) Trader Median, 5) Trader Mean, 6) Market Mean; each line corresponds to one of the nine dimensions of scores   plus the final MFI aggregate score; 1) Assortment, 2) Availability, 3) Price, 4) Resilience, 5) Competition, 6) Infrastructure, 7) Service,   8) Quality, 9) Access and Protection, and 10) MFI final score; the variable label describes each variable and its value range


# **m_fi_surveys_base_data_get**
> PagedSurveyResponsesDTO m_fi_surveys_base_data_get(survey_id=survey_id, page=page, page_size=page_size, env=env)

Get data that includes the core Market Functionality Index (MFI) fields only by Survey ID

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_mfi-surveys-basedata_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_survey_responses_dto import PagedSurveyResponsesDTO
from data_bridges_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.SurveysApi(api_client)
    survey_id = 56 # int | unique identifier for the collected data, as retrieved from /Surveys API. (optional)
    page = 1 # int | page number for paged results (optional) (default to 1)
    page_size = 20 # int | page size for paged results, default value is 20. (optional) (default to 20)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Get data that includes the core Market Functionality Index (MFI) fields only by Survey ID
        api_response = api_instance.m_fi_surveys_base_data_get(survey_id=survey_id, page=page, page_size=page_size, env=env)
        print("The response of SurveysApi->m_fi_surveys_base_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveysApi->m_fi_surveys_base_data_get: %s\n" % e)
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

# **m_fi_surveys_full_data_get**
> PagedSurveyResponsesDTO m_fi_surveys_full_data_get(survey_id=survey_id, format=format, page=page, page_size=page_size, env=env)

Get a full dataset that includes all the fields included in the survey in addition to the core Market Functionality Index (MFI) fields by Survey ID. To access this data, please contact global.mfi@wfp.org for authorization.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-TEC_Architecture_+_Service_Owner_approvals_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Official%20Use%20Only-yellow)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_mfi-surveys-fulldata_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_survey_responses_dto import PagedSurveyResponsesDTO
from data_bridges_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.SurveysApi(api_client)
    survey_id = 56 # int | unique identifier for the collected data, as retrieved from /Surveys API. (optional)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    page = 1 # int | page number for paged results (optional) (default to 1)
    page_size = 20 # int | page size for paged results, default value is 20. (optional) (default to 20)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Get a full dataset that includes all the fields included in the survey in addition to the core Market Functionality Index (MFI) fields by Survey ID. To access this data, please contact global.mfi@wfp.org for authorization.
        api_response = api_instance.m_fi_surveys_full_data_get(survey_id=survey_id, format=format, page=page, page_size=page_size, env=env)
        print("The response of SurveysApi->m_fi_surveys_full_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveysApi->m_fi_surveys_full_data_get: %s\n" % e)
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

# **m_fi_surveys_get**
> PagedSurveyListDTO m_fi_surveys_get(adm0_code=adm0_code, page=page, start_date=start_date, end_date=end_date, env=env)

Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all MFI surveys conducted in a country.   A date of reference, SurveyDate, for the data collection is set by the officer responsible for the upload for each survey.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_mfi-surveys_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_survey_list_dto import PagedSurveyListDTO
from data_bridges_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.SurveysApi(api_client)
    adm0_code = 0 # int | code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion (optional) (default to 0)
    page = 1 # int | page number for paged results (optional) (default to 1)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all MFI surveys conducted in a country.   A date of reference, SurveyDate, for the data collection is set by the officer responsible for the upload for each survey.
        api_response = api_instance.m_fi_surveys_get(adm0_code=adm0_code, page=page, start_date=start_date, end_date=end_date, env=env)
        print("The response of SurveysApi->m_fi_surveys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveysApi->m_fi_surveys_get: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **m_fi_surveys_processed_data_get**
> PagedProcessedDataDTO m_fi_surveys_processed_data_get(survey_id=survey_id, page=page, page_size=page_size, format=format, start_date=start_date, end_date=end_date, adm0_codes=adm0_codes, market_id=market_id, survey_type=survey_type, env=env)

Get a MFI processed data in long format; levels indicate the data aggregation level 1) Normalized Score, 2) Trader Aggregate Score,   3) Market Aggregate Score, 4) Trader Median, 5) Trader Mean, 6) Market Mean; each line corresponds to one of the nine dimensions of scores   plus the final MFI aggregate score; 1) Assortment, 2) Availability, 3) Price, 4) Resilience, 5) Competition, 6) Infrastructure, 7) Service,   8) Quality, 9) Access and Protection, and 10) MFI final score; the variable label describes each variable and its value range

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_mfi-surveys-processeddata_get\"      **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import data_bridges_client
from data_bridges_client.models.paged_processed_data_dto import PagedProcessedDataDTO
from data_bridges_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.wfp.org/vam-data-bridges/4.1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = data_bridges_client.Configuration(
    host = "https://api.wfp.org/vam-data-bridges/4.1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with data_bridges_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = data_bridges_client.SurveysApi(api_client)
    survey_id = 56 # int | The ID of the survey (optional)
    page = 1 # int | page number for paged results (optional) (default to 1)
    page_size = 20 # int |  (optional) (default to 20)
    format = 'json' # str | Output format: [JSON|CSV] Json is the default value (optional) (default to 'json')
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    adm0_codes = 'adm0_codes_example' # str | Code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion (optional)
    market_id = 56 # int | The ID of the market (optional)
    survey_type = 'survey_type_example' # str | The survey type (optional)
    env = 'env_example' # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
        # Get a MFI processed data in long format; levels indicate the data aggregation level 1) Normalized Score, 2) Trader Aggregate Score,   3) Market Aggregate Score, 4) Trader Median, 5) Trader Mean, 6) Market Mean; each line corresponds to one of the nine dimensions of scores   plus the final MFI aggregate score; 1) Assortment, 2) Availability, 3) Price, 4) Resilience, 5) Competition, 6) Infrastructure, 7) Service,   8) Quality, 9) Access and Protection, and 10) MFI final score; the variable label describes each variable and its value range
        api_response = api_instance.m_fi_surveys_processed_data_get(survey_id=survey_id, page=page, page_size=page_size, format=format, start_date=start_date, end_date=end_date, adm0_codes=adm0_codes, market_id=market_id, survey_type=survey_type, env=env)
        print("The response of SurveysApi->m_fi_surveys_processed_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SurveysApi->m_fi_surveys_processed_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| The ID of the survey | [optional] 
 **page** | **int**| page number for paged results | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 20]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] [default to &#39;json&#39;]
 **start_date** | **datetime**| Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \&quot;-\&quot; month \&quot;-\&quot; day (e.g. 2020/06/24) | [optional] 
 **end_date** | **datetime**| Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \&quot;-\&quot; month \&quot;-\&quot; day (e.g. 2020/06/24) | [optional] 
 **adm0_codes** | **str**| Code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion | [optional] 
 **market_id** | **int**| The ID of the market | [optional] 
 **survey_type** | **str**| The survey type | [optional] 
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - dev.api.vam.wfp.org | [optional] 

### Return type

[**PagedProcessedDataDTO**](PagedProcessedDataDTO.md)

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

