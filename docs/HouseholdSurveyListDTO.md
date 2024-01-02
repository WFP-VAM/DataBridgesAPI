# HouseholdSurveyListDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**survey_id** | **int** | The Id of the Survey | [optional] 
**survey_status_id** | **int** | The Id of the Survey status | [optional] 
**survey_start_date** | **datetime, none_type** | The date when the survey has started | [optional] 
**survey_end_date** | **datetime, none_type** | The date when the survey has ended | [optional] 
**survey_create_date** | **datetime** | The date when the survey has been uploaded in the Data Bridges platform | [optional] 
**survey_validation_report** | **str, none_type** | The detailed report on the validation performed on the survey schema | [optional] 
**survey_original_filename** | **str, none_type** | The filename of the survey CSV file | [optional] 
**xls_form_name** | **str, none_type** | The name of the XLSForm used to collect data | [optional] 
**base_xls_form_name** | **str, none_type** | The name of the base XLSForm used to build the XLSForm | [optional] 
**country_name** | **str, none_type** | The name of the country where the survey has taken place | [optional] 
**adm0_code** | **int** | The internal code of the country where the survey has taken place | [optional] 
**iso3_alpha3** | **str, none_type** | The ISO3 alpha code of the country where the survey has taken place | [optional] 
**user_name** | **str, none_type** | The name of the user that has uploaded the survey data | [optional] 
**approved_by** | **str, none_type** |  | [optional] 
**original_csv_file** | **str, none_type** | The link to download the original CSV file | [optional] 
**base_data** | **str, none_type** | The link to the JSON data reshaped on the base XLSForm | [optional] 
**survey_attributes** | [**[KeyNameDto], none_type**](KeyNameDto.md) |  | [optional] 
**organizations** | [**[KeyNameDto], none_type**](KeyNameDto.md) |  | [optional] 
**survey_modality_name** | **str, none_type** |  | [optional] 
**survey_category_name** | **str, none_type** |  | [optional] 
**survey_sub_category_name** | **str, none_type** |  | [optional] 
**survey_phase_name** | **str, none_type** |  | [optional] 
**survey_visibilty** | **str, none_type** |  | [optional] 
**is_continuous_monitoring** | **bool** |  | [optional] 
**survey_name** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


