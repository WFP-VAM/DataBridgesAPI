# KeyNameDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from data_bridges_client.models.key_name_dto import KeyNameDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeyNameDto from a JSON string
key_name_dto_instance = KeyNameDto.from_json(json)
# print the JSON string representation of the object
print KeyNameDto.to_json()

# convert the object into a dict
key_name_dto_dict = key_name_dto_instance.to_dict()
# create an instance of KeyNameDto from a dict
key_name_dto_form_dict = key_name_dto.from_dict(key_name_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


