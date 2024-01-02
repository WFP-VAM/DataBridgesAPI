# data_bridges_client.IncubationApi

All URIs are relative to *https://api.wfp.org/vam-data-bridges/1.4.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**household_draft_internal_base_data_get**](IncubationApi.md#household_draft_internal_base_data_get) | **GET** /Household/DraftInternalBaseData | Get data that includes the core household fields only by Survey ID
[**household_full_data_get**](IncubationApi.md#household_full_data_get) | **GET** /Household/FullData | Get a full dataset that includes all the fields included in the survey in addition to the core household fields by Survey ID. To access this data, please contact xxxx for authorization.
[**household_official_use_base_data_get**](IncubationApi.md#household_official_use_base_data_get) | **GET** /Household/OfficialUseBaseData | Get data that includes the core household fields only by Survey ID
[**household_public_base_data_get**](IncubationApi.md#household_public_base_data_get) | **GET** /Household/PublicBaseData | Get data that includes the core household fields only by Survey ID
[**household_surveys_get**](IncubationApi.md#household_surveys_get) | **GET** /Household/Surveys | Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all household surveys conducted in a country.   A date of reference, SurveyDate, for the data collection is set by the officer responsible of the upload for each survey.


# **household_draft_internal_base_data_get**
> SurveyDetailsDTO household_draft_internal_base_data_get()

Get data that includes the core household fields only by Survey ID

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Incubation-red)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Restricted-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Official%20Use%20Only-yellow)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_household-draftinternalbasedata_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import incubation_api
from data_bridges_client.model.survey_details_dto import SurveyDetailsDTO
from data_bridges_client.model.problem_details import ProblemDetails
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
    api_instance = incubation_api.IncubationApi(api_client)
    survey_id = 1 # int | unique identifier for the collected data, as retrieved from /Surveys API. (optional)
    page = 1 # int | page number for paged results (optional) if omitted the server will use the default value of 1
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data that includes the core household fields only by Survey ID
        api_response = api_instance.household_draft_internal_base_data_get(survey_id=survey_id, page=page, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling IncubationApi->household_draft_internal_base_data_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| unique identifier for the collected data, as retrieved from /Surveys API. | [optional]
 **page** | **int**| page number for paged results | [optional] if omitted the server will use the default value of 1
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - api.vam.wfp.org | [optional]

### Return type

[**SurveyDetailsDTO**](SurveyDetailsDTO.md)

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

# **household_full_data_get**
> SurveyDetailsDTO household_full_data_get()

Get a full dataset that includes all the fields included in the survey in addition to the core household fields by Survey ID. To access this data, please contact xxxx for authorization.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Incubation-red)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Restricted-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Official%20Use%20Only-yellow)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_household-fulldata_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import incubation_api
from data_bridges_client.model.survey_details_dto import SurveyDetailsDTO
from data_bridges_client.model.problem_details import ProblemDetails
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
    api_instance = incubation_api.IncubationApi(api_client)
    survey_id = 1 # int | unique identifier for the collected data, as retrieved from /Surveys API. (optional)
    format = "json" # str | Output format: [JSON|CSV] Json is the default value (optional) if omitted the server will use the default value of "json"
    page = 1 # int | page number for paged results (optional) if omitted the server will use the default value of 1
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a full dataset that includes all the fields included in the survey in addition to the core household fields by Survey ID. To access this data, please contact xxxx for authorization.
        api_response = api_instance.household_full_data_get(survey_id=survey_id, format=format, page=page, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling IncubationApi->household_full_data_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| unique identifier for the collected data, as retrieved from /Surveys API. | [optional]
 **format** | **str**| Output format: [JSON|CSV] Json is the default value | [optional] if omitted the server will use the default value of "json"
 **page** | **int**| page number for paged results | [optional] if omitted the server will use the default value of 1
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - api.vam.wfp.org | [optional]

### Return type

[**SurveyDetailsDTO**](SurveyDetailsDTO.md)

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

# **household_official_use_base_data_get**
> SurveyDetailsDTO household_official_use_base_data_get()

Get data that includes the core household fields only by Survey ID

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Incubation-red)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Restricted-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Official%20Use%20Only-yellow)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_household-officialusebasedata_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import incubation_api
from data_bridges_client.model.survey_details_dto import SurveyDetailsDTO
from data_bridges_client.model.problem_details import ProblemDetails
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
    api_instance = incubation_api.IncubationApi(api_client)
    survey_id = 1 # int | unique identifier for the collected data, as retrieved from /Surveys API. (optional)
    page = 1 # int | page number for paged results (optional) if omitted the server will use the default value of 1
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data that includes the core household fields only by Survey ID
        api_response = api_instance.household_official_use_base_data_get(survey_id=survey_id, page=page, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling IncubationApi->household_official_use_base_data_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| unique identifier for the collected data, as retrieved from /Surveys API. | [optional]
 **page** | **int**| page number for paged results | [optional] if omitted the server will use the default value of 1
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - api.vam.wfp.org | [optional]

### Return type

[**SurveyDetailsDTO**](SurveyDetailsDTO.md)

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

# **household_public_base_data_get**
> SurveyDetailsDTO household_public_base_data_get()

Get data that includes the core household fields only by Survey ID

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Incubation-red)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Restricted-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_household-publicbasedata_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import incubation_api
from data_bridges_client.model.survey_details_dto import SurveyDetailsDTO
from data_bridges_client.model.problem_details import ProblemDetails
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
    api_instance = incubation_api.IncubationApi(api_client)
    survey_id = 1 # int | unique identifier for the collected data, as retrieved from /Surveys API. (optional)
    page = 1 # int | page number for paged results (optional) if omitted the server will use the default value of 1
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data that includes the core household fields only by Survey ID
        api_response = api_instance.household_public_base_data_get(survey_id=survey_id, page=page, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling IncubationApi->household_public_base_data_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **survey_id** | **int**| unique identifier for the collected data, as retrieved from /Surveys API. | [optional]
 **page** | **int**| page number for paged results | [optional] if omitted the server will use the default value of 1
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - api.vam.wfp.org | [optional]

### Return type

[**SurveyDetailsDTO**](SurveyDetailsDTO.md)

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

# **household_surveys_get**
> [HouseholdSurveyListDTOPagedResult] household_surveys_get()

Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all household surveys conducted in a country.   A date of reference, SurveyDate, for the data collection is set by the officer responsible of the upload for each survey.

  [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Incubation-red)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

### Example

* OAuth Authentication (default):

```python
import time
import data_bridges_client
from data_bridges_client.api import incubation_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.household_survey_list_dto_paged_result import HouseholdSurveyListDTOPagedResult
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
    api_instance = incubation_api.IncubationApi(api_client)
    adm0_code = 0 # int | code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion (optional) if omitted the server will use the default value of 0
    page = 1 # int | page number for paged results (optional) if omitted the server will use the default value of 1
    start_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    end_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \"-\" month \"-\" day (e.g. 2020/06/24) (optional)
    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all household surveys conducted in a country.   A date of reference, SurveyDate, for the data collection is set by the officer responsible of the upload for each survey.
        api_response = api_instance.household_surveys_get(adm0_code=adm0_code, page=page, start_date=start_date, end_date=end_date, env=env)
        pprint(api_response)
    except data_bridges_client.ApiException as e:
        print("Exception when calling IncubationApi->household_surveys_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adm0_code** | **int**| code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion | [optional] if omitted the server will use the default value of 0
 **page** | **int**| page number for paged results | [optional] if omitted the server will use the default value of 1
 **start_date** | **datetime**| starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \&quot;-\&quot; month \&quot;-\&quot; day (e.g. 2020/06/24) | [optional]
 **end_date** | **datetime**| ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \&quot;-\&quot; month \&quot;-\&quot; day (e.g. 2020/06/24) | [optional]
 **env** | **str**| Environment.   * &#x60;prod&#x60; - api.vam.wfp.org   * &#x60;dev&#x60; - api.vam.wfp.org | [optional]

### Return type

[**[HouseholdSurveyListDTOPagedResult]**](HouseholdSurveyListDTOPagedResult.md)

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

