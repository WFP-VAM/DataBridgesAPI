# CommodityProcessingDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of the commodity | [optional] 
**name** | **str** | The name of the process | [optional] 

## Example

```python
from data_bridges_client.models.commodity_processing_dto import CommodityProcessingDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CommodityProcessingDTO from a JSON string
commodity_processing_dto_instance = CommodityProcessingDTO.from_json(json)
# print the JSON string representation of the object
print(CommodityProcessingDTO.to_json())

# convert the object into a dict
commodity_processing_dto_dict = commodity_processing_dto_instance.to_dict()
# create an instance of CommodityProcessingDTO from a dict
commodity_processing_dto_from_dict = CommodityProcessingDTO.from_dict(commodity_processing_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


