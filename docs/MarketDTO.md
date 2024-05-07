# MarketDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_id** | **int** | The internal ID of the market | [optional] 
**market_name** | **str** | The name of the market | [optional] 
**market_local_name** | **str** | The local name of the market | [optional] 
**market_latitude** | **float** | The decimal latitude | [optional] 
**market_longitude** | **float** | The decimal longitude | [optional] 
**admin1_name** | **str** | The name of the first level administrative division where the market is placed | [optional] 
**admin1_code** | **int** | The code of the first level administrative division where the market is placed | [optional] 
**admin2_name** | **str** | The name of the second level administrative division where the market is placed | [optional] 
**admin2_code** | **int** | The code of the second level administrative division where the market is placed | [optional] 

## Example

```python
from data_bridges_client.models.market_dto import MarketDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MarketDTO from a JSON string
market_dto_instance = MarketDTO.from_json(json)
# print the JSON string representation of the object
print(MarketDTO.to_json())

# convert the object into a dict
market_dto_dict = market_dto_instance.to_dict()
# create an instance of MarketDTO from a dict
market_dto_from_dict = MarketDTO.from_dict(market_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


