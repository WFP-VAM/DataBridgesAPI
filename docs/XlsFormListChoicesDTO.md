# XlsFormListChoicesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**choices** | [**List[XlsFormListChoiceDTO]**](XlsFormListChoiceDTO.md) |  | [optional] 

## Example

```python
from data_bridges_client.models.xls_form_list_choices_dto import XlsFormListChoicesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of XlsFormListChoicesDTO from a JSON string
xls_form_list_choices_dto_instance = XlsFormListChoicesDTO.from_json(json)
# print the JSON string representation of the object
print(XlsFormListChoicesDTO.to_json())

# convert the object into a dict
xls_form_list_choices_dto_dict = xls_form_list_choices_dto_instance.to_dict()
# create an instance of XlsFormListChoicesDTO from a dict
xls_form_list_choices_dto_from_dict = XlsFormListChoicesDTO.from_dict(xls_form_list_choices_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


