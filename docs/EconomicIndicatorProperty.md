# EconomicIndicatorProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**frequency** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**data_source** | **str** |  | [optional] 
**country_iso3** | **str** |  | [optional] 
**latest_value** | **float** |  | [optional] 
**latest_value_date** | **datetime** |  | [optional] 

## Example

```python
from data_bridges_client.models.economic_indicator_property import EconomicIndicatorProperty

# TODO update the JSON string below
json = "{}"
# create an instance of EconomicIndicatorProperty from a JSON string
economic_indicator_property_instance = EconomicIndicatorProperty.from_json(json)
# print the JSON string representation of the object
print EconomicIndicatorProperty.to_json()

# convert the object into a dict
economic_indicator_property_dict = economic_indicator_property_instance.to_dict()
# create an instance of EconomicIndicatorProperty from a dict
economic_indicator_property_form_dict = economic_indicator_property.from_dict(economic_indicator_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


