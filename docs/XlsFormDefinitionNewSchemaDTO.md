# XlsFormDefinitionNewSchemaDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**form_name** | **str** |  | [optional] 
**form_description** | **str** |  | [optional] 
**form_type** | **str** |  | [optional] 
**adm0_code** | **int** |  | [optional] 
**base_schema_id** | **int** |  | [optional] 
**category** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**fields** | [**List[XlsFormFieldsDTO]**](XlsFormFieldsDTO.md) |  | [optional] 

## Example

```python
from data_bridges_client.models.xls_form_definition_new_schema_dto import XlsFormDefinitionNewSchemaDTO

# TODO update the JSON string below
json = "{}"
# create an instance of XlsFormDefinitionNewSchemaDTO from a JSON string
xls_form_definition_new_schema_dto_instance = XlsFormDefinitionNewSchemaDTO.from_json(json)
# print the JSON string representation of the object
print(XlsFormDefinitionNewSchemaDTO.to_json())

# convert the object into a dict
xls_form_definition_new_schema_dto_dict = xls_form_definition_new_schema_dto_instance.to_dict()
# create an instance of XlsFormDefinitionNewSchemaDTO from a dict
xls_form_definition_new_schema_dto_from_dict = XlsFormDefinitionNewSchemaDTO.from_dict(xls_form_definition_new_schema_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


