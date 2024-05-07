# ViewExtendedAggregatedPricePagedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[ViewExtendedAggregatedPrice]**](ViewExtendedAggregatedPrice.md) |  | [optional] [readonly] 
**page** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.view_extended_aggregated_price_paged_result import ViewExtendedAggregatedPricePagedResult

# TODO update the JSON string below
json = "{}"
# create an instance of ViewExtendedAggregatedPricePagedResult from a JSON string
view_extended_aggregated_price_paged_result_instance = ViewExtendedAggregatedPricePagedResult.from_json(json)
# print the JSON string representation of the object
print(ViewExtendedAggregatedPricePagedResult.to_json())

# convert the object into a dict
view_extended_aggregated_price_paged_result_dict = view_extended_aggregated_price_paged_result_instance.to_dict()
# create an instance of ViewExtendedAggregatedPricePagedResult from a dict
view_extended_aggregated_price_paged_result_from_dict = ViewExtendedAggregatedPricePagedResult.from_dict(view_extended_aggregated_price_paged_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


