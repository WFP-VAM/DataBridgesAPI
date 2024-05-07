# EconomicDataDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from data_bridges_client.models.economic_data_dto import EconomicDataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EconomicDataDTO from a JSON string
economic_data_dto_instance = EconomicDataDTO.from_json(json)
# print the JSON string representation of the object
print(EconomicDataDTO.to_json())

# convert the object into a dict
economic_data_dto_dict = economic_data_dto_instance.to_dict()
# create an instance of EconomicDataDTO from a dict
economic_data_dto_from_dict = EconomicDataDTO.from_dict(economic_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


