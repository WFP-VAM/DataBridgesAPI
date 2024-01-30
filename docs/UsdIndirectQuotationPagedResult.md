# UsdIndirectQuotationPagedResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[UsdIndirectQuotation]**](UsdIndirectQuotation.md) |  | [optional] [readonly] 
**page** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from data_bridges_client.models.usd_indirect_quotation_paged_result import UsdIndirectQuotationPagedResult

# TODO update the JSON string below
json = "{}"
# create an instance of UsdIndirectQuotationPagedResult from a JSON string
usd_indirect_quotation_paged_result_instance = UsdIndirectQuotationPagedResult.from_json(json)
# print the JSON string representation of the object
print UsdIndirectQuotationPagedResult.to_json()

# convert the object into a dict
usd_indirect_quotation_paged_result_dict = usd_indirect_quotation_paged_result_instance.to_dict()
# create an instance of UsdIndirectQuotationPagedResult from a dict
usd_indirect_quotation_paged_result_form_dict = usd_indirect_quotation_paged_result.from_dict(usd_indirect_quotation_paged_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


