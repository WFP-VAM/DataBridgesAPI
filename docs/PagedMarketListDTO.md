# PagedMarketListDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** | The total number of items | [optional] 
**page** | **int** | The current page | [optional] 
**items** | [**List[MarketDTO]**](MarketDTO.md) | The list of markets | [optional] 

## Example

```python
from data_bridges_client.models.paged_market_list_dto import PagedMarketListDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PagedMarketListDTO from a JSON string
paged_market_list_dto_instance = PagedMarketListDTO.from_json(json)
# print the JSON string representation of the object
print(PagedMarketListDTO.to_json())

# convert the object into a dict
paged_market_list_dto_dict = paged_market_list_dto_instance.to_dict()
# create an instance of PagedMarketListDTO from a dict
paged_market_list_dto_from_dict = PagedMarketListDTO.from_dict(paged_market_list_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


