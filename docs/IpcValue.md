# IpcValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipc_id** | **int** |  | [optional] 
**ipc_year** | **int** |  | [optional] 
**ipc_update_date** | **datetime** |  | [optional] 
**iso3_alpha3** | **str** |  | [optional] 
**ipc_country_name** | **str** |  | [optional] 
**ipc_area_name** | **str** |  | [optional] 
**ipc_phase3_population** | **int** |  | [optional] 
**ipc_phase4_population** | **int** |  | [optional] 
**ipc_phase5_population** | **int** |  | [optional] 
**ipc_phase35population** | **int** |  | [optional] 
**ipc_phase45population** | **int** |  | [optional] 
**ipc_phase3_percentage** | **float** |  | [optional] 
**ipc_phase4_percentage** | **float** |  | [optional] 
**ipc_phase5_percentage** | **float** |  | [optional] 
**ipc_phase35percentage** | **float** |  | [optional] 
**ipc_phase45percentage** | **float** |  | [optional] 
**ipc_analysed_population** | **int** |  | [optional] 
**ipc_analysed_percentage** | **float** |  | [optional] 
**ipc_analysis_comment** | **str** |  | [optional] 
**ipc_data_type** | **str** |  | [optional] 
**ipc_data_source** | **str** |  | [optional] 
**ipc_reference_period** | **str** |  | [optional] 
**ipc_create_date** | **datetime** |  | [optional] 
**ipc_show_on_data_viz** | **bool** |  | [optional] 
**ipc_is_latest_value** | **bool** |  | [optional] 

## Example

```python
from data_bridges_client.models.ipc_value import IpcValue

# TODO update the JSON string below
json = "{}"
# create an instance of IpcValue from a JSON string
ipc_value_instance = IpcValue.from_json(json)
# print the JSON string representation of the object
print(IpcValue.to_json())

# convert the object into a dict
ipc_value_dict = ipc_value_instance.to_dict()
# create an instance of IpcValue from a dict
ipc_value_from_dict = IpcValue.from_dict(ipc_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


