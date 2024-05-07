# RpmeAssessmentPagedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RpmeAssessment]**](RpmeAssessment.md) |  | [optional] [readonly] 
**page** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.rpme_assessment_paged_result import RpmeAssessmentPagedResult

# TODO update the JSON string below
json = "{}"
# create an instance of RpmeAssessmentPagedResult from a JSON string
rpme_assessment_paged_result_instance = RpmeAssessmentPagedResult.from_json(json)
# print the JSON string representation of the object
print(RpmeAssessmentPagedResult.to_json())

# convert the object into a dict
rpme_assessment_paged_result_dict = rpme_assessment_paged_result_instance.to_dict()
# create an instance of RpmeAssessmentPagedResult from a dict
rpme_assessment_paged_result_from_dict = RpmeAssessmentPagedResult.from_dict(rpme_assessment_paged_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


