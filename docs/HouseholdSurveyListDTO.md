# HouseholdSurveyListDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**survey_id** | **int** | The Id of the Survey | [optional] 
**survey_status_id** | **int** | The Id of the Survey status | [optional] 
**survey_start_date** | **datetime** | The date when the survey has started | [optional] 
**survey_end_date** | **datetime** | The date when the survey has ended | [optional] 
**survey_create_date** | **datetime** | The date when the survey has been uploaded in the Data Bridges platform | [optional] 
**survey_validation_report** | **str** | The detailed report on the validation performed on the survey schema | [optional] 
**survey_original_filename** | **str** | The filename of the survey CSV file | [optional] 
**xls_form_name** | **str** | The name of the XLSForm used to collect data | [optional] 
**base_xls_form_name** | **str** | The name of the base XLSForm used to build the XLSForm | [optional] 
**country_name** | **str** | The name of the country where the survey has taken place | [optional] 
**adm0_code** | **int** | The internal code of the country where the survey has taken place | [optional] 
**iso3_alpha3** | **str** | The ISO3 alpha code of the country where the survey has taken place | [optional] 
**user_name** | **str** | The name of the user that has uploaded the survey data | [optional] 
**approved_by** | **str** |  | [optional] 
**original_csv_file** | **str** | The link to download the original CSV file | [optional] 
**base_data** | **str** | The link to the JSON data reshaped on the base XLSForm | [optional] 
**survey_attributes** | [**List[KeyNameDto]**](KeyNameDto.md) |  | [optional] 
**organizations** | [**List[KeyNameDto]**](KeyNameDto.md) |  | [optional] 
**survey_modality_name** | **str** |  | [optional] 
**survey_category_name** | **str** |  | [optional] 
**survey_sub_category_name** | **str** |  | [optional] 
**survey_phase_name** | **str** |  | [optional] 
**survey_visibilty** | **str** |  | [optional] 
**is_continuous_monitoring** | **bool** |  | [optional] 
**survey_name** | **str** |  | [optional] 

## Example

```python
from data_bridges_client.models.household_survey_list_dto import HouseholdSurveyListDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HouseholdSurveyListDTO from a JSON string
household_survey_list_dto_instance = HouseholdSurveyListDTO.from_json(json)
# print the JSON string representation of the object
print HouseholdSurveyListDTO.to_json()

# convert the object into a dict
household_survey_list_dto_dict = household_survey_list_dto_instance.to_dict()
# create an instance of HouseholdSurveyListDTO from a dict
household_survey_list_dto_form_dict = household_survey_list_dto.from_dict(household_survey_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


