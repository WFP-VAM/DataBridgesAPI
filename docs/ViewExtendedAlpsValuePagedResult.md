# ViewExtendedAlpsValuePagedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ViewExtendedAlpsValue]**](ViewExtendedAlpsValue.md) |  | [optional] [readonly] 
**page** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.view_extended_alps_value_paged_result import ViewExtendedAlpsValuePagedResult

# TODO update the JSON string below
json = "{}"
# create an instance of ViewExtendedAlpsValuePagedResult from a JSON string
view_extended_alps_value_paged_result_instance = ViewExtendedAlpsValuePagedResult.from_json(json)
# print the JSON string representation of the object
print ViewExtendedAlpsValuePagedResult.to_json()

# convert the object into a dict
view_extended_alps_value_paged_result_dict = view_extended_alps_value_paged_result_instance.to_dict()
# create an instance of ViewExtendedAlpsValuePagedResult from a dict
view_extended_alps_value_paged_result_form_dict = view_extended_alps_value_paged_result.from_dict(view_extended_alps_value_paged_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


