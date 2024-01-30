# RpmeVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_id** | **int** |  | [optional] 
**variable_name** | **str** |  | [optional] 
**variable_description** | **str** |  | [optional] 
**dimension_id** | **int** |  | [optional] 
**dimension_name** | **str** |  | [optional] 
**level_id** | **int** |  | [optional] 
**level_name** | **str** |  | [optional] 
**survey_mode_id** | **int** |  | [optional] 
**survey_mode_name** | **str** |  | [optional] 

## Example

```python
from data_bridges_client.models.rpme_variable import RpmeVariable

# TODO update the JSON string below
json = "{}"
# create an instance of RpmeVariable from a JSON string
rpme_variable_instance = RpmeVariable.from_json(json)
# print the JSON string representation of the object
print RpmeVariable.to_json()

# convert the object into a dict
rpme_variable_dict = rpme_variable_instance.to_dict()
# create an instance of RpmeVariable from a dict
rpme_variable_form_dict = rpme_variable.from_dict(rpme_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


