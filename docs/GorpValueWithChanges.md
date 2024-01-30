# GorpValueWithChanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | [optional] 
**month** | **str** |  | [optional] 
**region_name** | **str** |  | [optional] 
**actual_value** | **float** |  | [optional] 
**baseline_value** | **float** |  | [optional] 
**percentage_change** | **float** |  | [optional] 
**absolute_change** | **float** |  | [optional] 
**comments** | **str** |  | [optional] 
**number_of_countries** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.gorp_value_with_changes import GorpValueWithChanges

# TODO update the JSON string below
json = "{}"
# create an instance of GorpValueWithChanges from a JSON string
gorp_value_with_changes_instance = GorpValueWithChanges.from_json(json)
# print the JSON string representation of the object
print GorpValueWithChanges.to_json()

# convert the object into a dict
gorp_value_with_changes_dict = gorp_value_with_changes_instance.to_dict()
# create an instance of GorpValueWithChanges from a dict
gorp_value_with_changes_form_dict = gorp_value_with_changes.from_dict(gorp_value_with_changes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


