# GorpGlobalApiDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gorp_date** | **str** |  | [optional] 
**gorp_region_name** | **str** |  | [optional] 
**gorp_total_value** | **float** |  | [optional] 
**number_of_countries** | **int** |  | [optional] 
**gorp_comment** | **str** |  | [optional] 

## Example

```python
from data_bridges_client.models.gorp_global_api_dto import GorpGlobalApiDto

# TODO update the JSON string below
json = "{}"
# create an instance of GorpGlobalApiDto from a JSON string
gorp_global_api_dto_instance = GorpGlobalApiDto.from_json(json)
# print the JSON string representation of the object
print(GorpGlobalApiDto.to_json())

# convert the object into a dict
gorp_global_api_dto_dict = gorp_global_api_dto_instance.to_dict()
# create an instance of GorpGlobalApiDto from a dict
gorp_global_api_dto_from_dict = GorpGlobalApiDto.from_dict(gorp_global_api_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


