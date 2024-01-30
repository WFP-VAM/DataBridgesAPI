# NearbyMarketsDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_id** | **int** | The internal ID of the market | [optional] 
**market_name** | **str** | The name of the market | [optional] 
**distance** | **float** | The distance in meters of the market from the provided point | [optional] 

## Example

```python
from data_bridges_client.models.nearby_markets_dto import NearbyMarketsDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NearbyMarketsDTO from a JSON string
nearby_markets_dto_instance = NearbyMarketsDTO.from_json(json)
# print the JSON string representation of the object
print NearbyMarketsDTO.to_json()

# convert the object into a dict
nearby_markets_dto_dict = nearby_markets_dto_instance.to_dict()
# create an instance of NearbyMarketsDTO from a dict
nearby_markets_dto_form_dict = nearby_markets_dto.from_dict(nearby_markets_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


