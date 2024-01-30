# IpcValuePagedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[IpcValue]**](IpcValue.md) |  | [optional] [readonly] 
**page** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.ipc_value_paged_result import IpcValuePagedResult

# TODO update the JSON string below
json = "{}"
# create an instance of IpcValuePagedResult from a JSON string
ipc_value_paged_result_instance = IpcValuePagedResult.from_json(json)
# print the JSON string representation of the object
print IpcValuePagedResult.to_json()

# convert the object into a dict
ipc_value_paged_result_dict = ipc_value_paged_result_instance.to_dict()
# create an instance of IpcValuePagedResult from a dict
ipc_value_paged_result_form_dict = ipc_value_paged_result.from_dict(ipc_value_paged_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


