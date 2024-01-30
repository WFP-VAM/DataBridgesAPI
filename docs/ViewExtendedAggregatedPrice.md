# ViewExtendedAggregatedPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commodity_id** | **int** |  | [optional] 
**market_id** | **int** |  | [optional] 
**price_type_id** | **int** |  | [optional] 
**commodity_unit_id** | **int** |  | [optional] 
**currency_id** | **int** |  | [optional] 
**adm0_code** | **int** |  | [optional] 
**commodity_date_week** | **int** |  | [optional] 
**commodity_date_month** | **int** |  | [optional] 
**commodity_date_year** | **int** |  | [optional] 
**commodity_price_date** | **datetime** |  | [optional] 
**commodity_name** | **str** |  | [optional] 
**market_name** | **str** |  | [optional] 
**price_type_name** | **str** |  | [optional] 
**commodity_unit_name** | **str** |  | [optional] 
**currency_name** | **str** |  | [optional] 
**country_iso3** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**commodity_price_source_name** | **str** |  | [optional] 
**original_frequency** | **str** |  | [optional] 
**commodity_price** | **float** |  | [optional] 
**commodity_price_observations** | **int** |  | [optional] 
**commodity_price_flag** | **str** |  | [optional] 

## Example

```python
from data_bridges_client.models.view_extended_aggregated_price import ViewExtendedAggregatedPrice

# TODO update the JSON string below
json = "{}"
# create an instance of ViewExtendedAggregatedPrice from a JSON string
view_extended_aggregated_price_instance = ViewExtendedAggregatedPrice.from_json(json)
# print the JSON string representation of the object
print ViewExtendedAggregatedPrice.to_json()

# convert the object into a dict
view_extended_aggregated_price_dict = view_extended_aggregated_price_instance.to_dict()
# create an instance of ViewExtendedAggregatedPrice from a dict
view_extended_aggregated_price_form_dict = view_extended_aggregated_price.from_dict(view_extended_aggregated_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


