# UsdIndirectQuotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | the ISO3 code for the currency, based on ISO4217 | [optional] 
**adm0_code** | **int** |  | [optional] 
**country_iso3** | **str** |  | [optional] 
**is_official** | **bool** | The field IsOfficial is a boolean which can be set to true for the Trading Economics data and to false for the data coming from a commodity saved in the DataBridges database | [optional] 
**frequency** | **str** | (it’s from the reporting commodity named Exchange Rate | [optional] 
**value** | **float** |  | [optional] 
**var_date** | **datetime** |  | [optional] 

## Example

```python
from data_bridges_client.models.usd_indirect_quotation import UsdIndirectQuotation

# TODO update the JSON string below
json = "{}"
# create an instance of UsdIndirectQuotation from a JSON string
usd_indirect_quotation_instance = UsdIndirectQuotation.from_json(json)
# print the JSON string representation of the object
print UsdIndirectQuotation.to_json()

# convert the object into a dict
usd_indirect_quotation_dict = usd_indirect_quotation_instance.to_dict()
# create an instance of UsdIndirectQuotation from a dict
usd_indirect_quotation_form_dict = usd_indirect_quotation.from_dict(usd_indirect_quotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


