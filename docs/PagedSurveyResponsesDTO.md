# PagedSurveyResponsesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** | The total number of responses | [optional] 
**page** | **int** | The current page | [optional] 
**items** | **List[object]** | The list of survey responses | [optional] 

## Example

```python
from data_bridges_client.models.paged_survey_responses_dto import PagedSurveyResponsesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PagedSurveyResponsesDTO from a JSON string
paged_survey_responses_dto_instance = PagedSurveyResponsesDTO.from_json(json)
# print the JSON string representation of the object
print PagedSurveyResponsesDTO.to_json()

# convert the object into a dict
paged_survey_responses_dto_dict = paged_survey_responses_dto_instance.to_dict()
# create an instance of PagedSurveyResponsesDTO from a dict
paged_survey_responses_dto_form_dict = paged_survey_responses_dto.from_dict(paged_survey_responses_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


