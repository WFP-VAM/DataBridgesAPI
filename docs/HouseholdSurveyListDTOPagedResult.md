# HouseholdSurveyListDTOPagedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[HouseholdSurveyListDTO]**](HouseholdSurveyListDTO.md) |  | [optional] [readonly] 
**page** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.household_survey_list_dto_paged_result import HouseholdSurveyListDTOPagedResult

# TODO update the JSON string below
json = "{}"
# create an instance of HouseholdSurveyListDTOPagedResult from a JSON string
household_survey_list_dto_paged_result_instance = HouseholdSurveyListDTOPagedResult.from_json(json)
# print the JSON string representation of the object
print HouseholdSurveyListDTOPagedResult.to_json()

# convert the object into a dict
household_survey_list_dto_paged_result_dict = household_survey_list_dto_paged_result_instance.to_dict()
# create an instance of HouseholdSurveyListDTOPagedResult from a dict
household_survey_list_dto_paged_result_form_dict = household_survey_list_dto_paged_result.from_dict(household_survey_list_dto_paged_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


