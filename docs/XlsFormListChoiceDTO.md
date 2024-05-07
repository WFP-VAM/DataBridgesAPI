# XlsFormListChoiceDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from data_bridges_client.models.xls_form_list_choice_dto import XlsFormListChoiceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of XlsFormListChoiceDTO from a JSON string
xls_form_list_choice_dto_instance = XlsFormListChoiceDTO.from_json(json)
# print the JSON string representation of the object
print(XlsFormListChoiceDTO.to_json())

# convert the object into a dict
xls_form_list_choice_dto_dict = xls_form_list_choice_dto_instance.to_dict()
# create an instance of XlsFormListChoiceDTO from a dict
xls_form_list_choice_dto_from_dict = XlsFormListChoiceDTO.from_dict(xls_form_list_choice_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


