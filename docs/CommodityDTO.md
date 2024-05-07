# CommodityDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of the commodity | [optional] 
**parent_id** | **int** | The internal parent ID of the commodity | [optional] 
**name** | **str** | The name of the commodity | [optional] 
**coicop2018** | **str** | The COICOP 2018 definition | [optional] 
**supply** | **int** |  | [optional] 
**category_id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**update_date** | **datetime** |  | [optional] 
**qualities** | [**List[CommodityQualityDTO]**](CommodityQualityDTO.md) |  | [optional] 
**processing** | [**List[CommodityProcessingDTO]**](CommodityProcessingDTO.md) |  | [optional] 

## Example

```python
from data_bridges_client.models.commodity_dto import CommodityDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CommodityDTO from a JSON string
commodity_dto_instance = CommodityDTO.from_json(json)
# print the JSON string representation of the object
print(CommodityDTO.to_json())

# convert the object into a dict
commodity_dto_dict = commodity_dto_instance.to_dict()
# create an instance of CommodityDTO from a dict
commodity_dto_from_dict = CommodityDTO.from_dict(commodity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


