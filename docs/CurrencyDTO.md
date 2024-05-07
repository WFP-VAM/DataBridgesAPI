# CurrencyDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of the unit | [optional] 
**name** | **str** | The name of the unit | [optional] 
**extended_name** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**update_date** | **datetime** |  | [optional] 

## Example

```python
from data_bridges_client.models.currency_dto import CurrencyDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CurrencyDTO from a JSON string
currency_dto_instance = CurrencyDTO.from_json(json)
# print the JSON string representation of the object
print(CurrencyDTO.to_json())

# convert the object into a dict
currency_dto_dict = currency_dto_instance.to_dict()
# create an instance of CurrencyDTO from a dict
currency_dto_from_dict = CurrencyDTO.from_dict(currency_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


