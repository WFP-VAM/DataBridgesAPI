# EconomicIndicatorPropertyPagedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EconomicIndicatorProperty]**](EconomicIndicatorProperty.md) |  | [optional] [readonly] 
**page** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.economic_indicator_property_paged_result import EconomicIndicatorPropertyPagedResult

# TODO update the JSON string below
json = "{}"
# create an instance of EconomicIndicatorPropertyPagedResult from a JSON string
economic_indicator_property_paged_result_instance = EconomicIndicatorPropertyPagedResult.from_json(json)
# print the JSON string representation of the object
print EconomicIndicatorPropertyPagedResult.to_json()

# convert the object into a dict
economic_indicator_property_paged_result_dict = economic_indicator_property_paged_result_instance.to_dict()
# create an instance of EconomicIndicatorPropertyPagedResult from a dict
economic_indicator_property_paged_result_form_dict = economic_indicator_property_paged_result.from_dict(economic_indicator_property_paged_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


