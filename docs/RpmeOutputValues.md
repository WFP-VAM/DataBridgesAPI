# RpmeOutputValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable_id** | **int** |  | [optional] 
**output_value** | **float** |  | [optional] 

## Example

```python
from data_bridges_client.models.rpme_output_values import RpmeOutputValues

# TODO update the JSON string below
json = "{}"
# create an instance of RpmeOutputValues from a JSON string
rpme_output_values_instance = RpmeOutputValues.from_json(json)
# print the JSON string representation of the object
print RpmeOutputValues.to_json()

# convert the object into a dict
rpme_output_values_dict = rpme_output_values_instance.to_dict()
# create an instance of RpmeOutputValues from a dict
rpme_output_values_form_dict = rpme_output_values.from_dict(rpme_output_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


