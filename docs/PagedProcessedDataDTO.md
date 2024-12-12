# PagedProcessedDataDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** | The total number of items | [optional] 
**page** | **int** | The current page | [optional] 
**scroll_id** | **int** |  | [optional] 
**items** | [**List[MFIProcessedDataDTO]**](MFIProcessedDataDTO.md) | The list of processed data | [optional] 

## Example

```python
from data_bridges_client.models.paged_processed_data_dto import PagedProcessedDataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PagedProcessedDataDTO from a JSON string
paged_processed_data_dto_instance = PagedProcessedDataDTO.from_json(json)
# print the JSON string representation of the object
print(PagedProcessedDataDTO.to_json())

# convert the object into a dict
paged_processed_data_dto_dict = paged_processed_data_dto_instance.to_dict()
# create an instance of PagedProcessedDataDTO from a dict
paged_processed_data_dto_from_dict = PagedProcessedDataDTO.from_dict(paged_processed_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


