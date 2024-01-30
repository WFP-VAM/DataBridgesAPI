# RpmeVariablePagedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RpmeVariable]**](RpmeVariable.md) |  | [optional] [readonly] 
**page** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.rpme_variable_paged_result import RpmeVariablePagedResult

# TODO update the JSON string below
json = "{}"
# create an instance of RpmeVariablePagedResult from a JSON string
rpme_variable_paged_result_instance = RpmeVariablePagedResult.from_json(json)
# print the JSON string representation of the object
print RpmeVariablePagedResult.to_json()

# convert the object into a dict
rpme_variable_paged_result_dict = rpme_variable_paged_result_instance.to_dict()
# create an instance of RpmeVariablePagedResult from a dict
rpme_variable_paged_result_form_dict = rpme_variable_paged_result.from_dict(rpme_variable_paged_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


