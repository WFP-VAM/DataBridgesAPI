# XlsFormFieldsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**choice_list** | [**XlsFormListChoicesDTO**](XlsFormListChoicesDTO.md) |  | [optional] 

## Example

```python
from data_bridges_client.models.xls_form_fields_dto import XlsFormFieldsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of XlsFormFieldsDTO from a JSON string
xls_form_fields_dto_instance = XlsFormFieldsDTO.from_json(json)
# print the JSON string representation of the object
print(XlsFormFieldsDTO.to_json())

# convert the object into a dict
xls_form_fields_dto_dict = xls_form_fields_dto_instance.to_dict()
# create an instance of XlsFormFieldsDTO from a dict
xls_form_fields_dto_from_dict = XlsFormFieldsDTO.from_dict(xls_form_fields_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


