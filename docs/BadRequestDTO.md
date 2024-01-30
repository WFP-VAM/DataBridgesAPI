# BadRequestDTO



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | The error message returned by the application | [optional] 

## Example

```python
from data_bridges_client.models.bad_request_dto import BadRequestDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestDTO from a JSON string
bad_request_dto_instance = BadRequestDTO.from_json(json)
# print the JSON string representation of the object
print BadRequestDTO.to_json()

# convert the object into a dict
bad_request_dto_dict = bad_request_dto_instance.to_dict()
# create an instance of BadRequestDTO from a dict
bad_request_dto_form_dict = bad_request_dto.from_dict(bad_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


