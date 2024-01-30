# XlsFormDefinitionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xls_form_field_name** | **str** |  | [optional] 
**xls_form_field_label** | **str** |  | [optional] 
**xls_form_field_row** | **int** |  | [optional] 
**xls_form_field_type** | **str** |  | [optional] 
**xls_form_list_id** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.xls_form_definition_dto import XlsFormDefinitionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of XlsFormDefinitionDTO from a JSON string
xls_form_definition_dto_instance = XlsFormDefinitionDTO.from_json(json)
# print the JSON string representation of the object
print XlsFormDefinitionDTO.to_json()

# convert the object into a dict
xls_form_definition_dto_dict = xls_form_definition_dto_instance.to_dict()
# create an instance of XlsFormDefinitionDTO from a dict
xls_form_definition_dto_form_dict = xls_form_definition_dto.from_dict(xls_form_definition_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


