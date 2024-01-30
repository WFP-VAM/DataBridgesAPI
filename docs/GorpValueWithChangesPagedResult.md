# GorpValueWithChangesPagedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GorpValueWithChanges]**](GorpValueWithChanges.md) |  | [optional] [readonly] 
**page** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.gorp_value_with_changes_paged_result import GorpValueWithChangesPagedResult

# TODO update the JSON string below
json = "{}"
# create an instance of GorpValueWithChangesPagedResult from a JSON string
gorp_value_with_changes_paged_result_instance = GorpValueWithChangesPagedResult.from_json(json)
# print the JSON string representation of the object
print GorpValueWithChangesPagedResult.to_json()

# convert the object into a dict
gorp_value_with_changes_paged_result_dict = gorp_value_with_changes_paged_result_instance.to_dict()
# create an instance of GorpValueWithChangesPagedResult from a dict
gorp_value_with_changes_paged_result_form_dict = gorp_value_with_changes_paged_result.from_dict(gorp_value_with_changes_paged_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


