# MarketGeoJsonRoot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**features** | [**List[Feature]**](Feature.md) |  | [optional] 
**bbox** | **object** |  | [optional] 

## Example

```python
from data_bridges_client.models.market_geo_json_root import MarketGeoJsonRoot

# TODO update the JSON string below
json = "{}"
# create an instance of MarketGeoJsonRoot from a JSON string
market_geo_json_root_instance = MarketGeoJsonRoot.from_json(json)
# print the JSON string representation of the object
print(MarketGeoJsonRoot.to_json())

# convert the object into a dict
market_geo_json_root_dict = market_geo_json_root_instance.to_dict()
# create an instance of MarketGeoJsonRoot from a dict
market_geo_json_root_from_dict = MarketGeoJsonRoot.from_dict(market_geo_json_root_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


