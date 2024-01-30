# PagedEconomicDataDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** | The total number of items | [optional] 
**page** | **int** | The current page | [optional] 
**unit** | **str** |  | [optional] 
**frequency** | **str** |  | [optional] 
**data_source** | **str** |  | [optional] 
**items** | [**List[EconomicDataDTO]**](EconomicDataDTO.md) | The list of paged items | [optional] 

## Example

```python
from data_bridges_client.models.paged_economic_data_dto import PagedEconomicDataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of PagedEconomicDataDTO from a JSON string
paged_economic_data_dto_instance = PagedEconomicDataDTO.from_json(json)
# print the JSON string representation of the object
print PagedEconomicDataDTO.to_json()

# convert the object into a dict
paged_economic_data_dto_dict = paged_economic_data_dto_instance.to_dict()
# create an instance of PagedEconomicDataDTO from a dict
paged_economic_data_dto_form_dict = paged_economic_data_dto.from_dict(paged_economic_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


