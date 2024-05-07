# ViewExtendedAlpsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commodity_id** | **int** |  | [optional] 
**market_id** | **int** |  | [optional] 
**price_type_id** | **int** |  | [optional] 
**commodity_unit_id** | **int** |  | [optional] 
**currency_id** | **int** |  | [optional] 
**adm0_code** | **int** |  | [optional] 
**country_name** | **str** |  | [optional] 
**commodity_price_date_year** | **int** |  | [optional] 
**commodity_price_date_month** | **int** |  | [optional] 
**commodity_price_date_week** | **int** |  | [optional] 
**commodity_price_date** | **datetime** |  | [optional] 
**commodity_name** | **str** |  | [optional] 
**market_name** | **str** |  | [optional] 
**price_type_name** | **str** |  | [optional] 
**commodity_unit_name** | **str** |  | [optional] 
**currency_name** | **str** |  | [optional] 
**analysis_value_estimated_price** | **float** |  | [optional] 
**analysis_value_pewi_value** | **float** |  | [optional] 
**analysis_value_price_flag** | **str** |  | [optional] 

## Example

```python
from data_bridges_client.models.view_extended_alps_value import ViewExtendedAlpsValue

# TODO update the JSON string below
json = "{}"
# create an instance of ViewExtendedAlpsValue from a JSON string
view_extended_alps_value_instance = ViewExtendedAlpsValue.from_json(json)
# print the JSON string representation of the object
print(ViewExtendedAlpsValue.to_json())

# convert the object into a dict
view_extended_alps_value_dict = view_extended_alps_value_instance.to_dict()
# create an instance of ViewExtendedAlpsValue from a dict
view_extended_alps_value_from_dict = ViewExtendedAlpsValue.from_dict(view_extended_alps_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


