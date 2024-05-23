# CommodityPriceDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal ID of the commodity | [optional] 
**commodity_id** | **int** |  | [optional] 
**market_id** | **int** |  | [optional] 
**price_type_id** | **int** |  | [optional] 
**commodity_unit_id** | **int** |  | [optional] 
**currency_id** | **int** |  | [optional] 
**commodity_name** | **str** |  | [optional] 
**market_name** | **str** |  | [optional] 
**price_type_name** | **str** |  | [optional] 
**unit_name** | **str** |  | [optional] 
**currency_name** | **str** |  | [optional] 
**original_frequency** | **str** |  | [optional] 
**adm0_code** | **int** |  | [optional] 
**country_iso3** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**commodity_price** | **float** |  | [optional] 
**commodity_price_source_name** | **str** |  | [optional] 
**commodity_price_metadata** | **object** |  | [optional] 
**commodity_price_date** | **datetime** |  | [optional] 
**commodity_price_observations** | **int** |  | [optional] 
**commodity_price_date_day** | **int** |  | [optional] 
**commodity_price_date_week** | **int** |  | [optional] 
**commodity_price_date_month** | **int** |  | [optional] 
**commodity_price_date_year** | **int** |  | [optional] 
**commodity_price_insert_date** | **datetime** |  | [optional] 
**commodity_price_flag** | **str** |  | [optional] 

## Example

```python
from data_bridges_client.models.commodity_price_dto import CommodityPriceDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CommodityPriceDTO from a JSON string
commodity_price_dto_instance = CommodityPriceDTO.from_json(json)
# print the JSON string representation of the object
print(CommodityPriceDTO.to_json())

# convert the object into a dict
commodity_price_dto_dict = commodity_price_dto_instance.to_dict()
# create an instance of CommodityPriceDTO from a dict
commodity_price_dto_from_dict = CommodityPriceDTO.from_dict(commodity_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


