# GorpCountryApiDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gorp_date** | **str** |  | [optional] 
**country_office_iso3** | **str** |  | [optional] 
**gorp_total_value** | **float** |  | [optional] 
**gorp_comment** | **str** |  | [optional] 

## Example

```python
from data_bridges_client.models.gorp_country_api_dto import GorpCountryApiDto

# TODO update the JSON string below
json = "{}"
# create an instance of GorpCountryApiDto from a JSON string
gorp_country_api_dto_instance = GorpCountryApiDto.from_json(json)
# print the JSON string representation of the object
print(GorpCountryApiDto.to_json())

# convert the object into a dict
gorp_country_api_dto_dict = gorp_country_api_dto_instance.to_dict()
# create an instance of GorpCountryApiDto from a dict
gorp_country_api_dto_from_dict = GorpCountryApiDto.from_dict(gorp_country_api_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


