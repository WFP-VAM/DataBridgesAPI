# PagedSurveyListDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** | The total number of items | [optional] 
**page** | **int** | The current page | [optional] 
**items** | [**List[SurveyListDTO]**](SurveyListDTO.md) | The list of surveys | [optional] 

## Example

```python
from data_bridges_client.models.paged_survey_list_dto import PagedSurveyListDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PagedSurveyListDTO from a JSON string
paged_survey_list_dto_instance = PagedSurveyListDTO.from_json(json)
# print the JSON string representation of the object
print PagedSurveyListDTO.to_json()

# convert the object into a dict
paged_survey_list_dto_dict = paged_survey_list_dto_instance.to_dict()
# create an instance of PagedSurveyListDTO from a dict
paged_survey_list_dto_form_dict = paged_survey_list_dto.from_dict(paged_survey_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


