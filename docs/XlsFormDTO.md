# XlsFormDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xls_form_id** | **int** |  | [optional] 
**xls_form_name** | **str** |  | [optional] 
**xls_form_create_date** | **datetime** |  | [optional] 
**user_name** | **str** |  | [optional] 
**xls_form_source_file** | **str** |  | [optional] 
**xls_form_is_base_schema** | **bool** |  | [optional] 
**adm0_code** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.xls_form_dto import XlsFormDTO

# TODO update the JSON string below
json = "{}"
# create an instance of XlsFormDTO from a JSON string
xls_form_dto_instance = XlsFormDTO.from_json(json)
# print the JSON string representation of the object
print XlsFormDTO.to_json()

# convert the object into a dict
xls_form_dto_dict = xls_form_dto_instance.to_dict()
# create an instance of XlsFormDTO from a dict
xls_form_dto_form_dict = xls_form_dto.from_dict(xls_form_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


