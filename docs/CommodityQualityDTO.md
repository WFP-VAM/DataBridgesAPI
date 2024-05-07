# CommodityQualityDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of the commodity | [optional] 
**name** | **str** | The name of the commodity | [optional] 

## Example

```python
from data_bridges_client.models.commodity_quality_dto import CommodityQualityDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CommodityQualityDTO from a JSON string
commodity_quality_dto_instance = CommodityQualityDTO.from_json(json)
# print the JSON string representation of the object
print(CommodityQualityDTO.to_json())

# convert the object into a dict
commodity_quality_dto_dict = commodity_quality_dto_instance.to_dict()
# create an instance of CommodityQualityDTO from a dict
commodity_quality_dto_from_dict = CommodityQualityDTO.from_dict(commodity_quality_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


