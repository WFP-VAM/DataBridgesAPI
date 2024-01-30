# MFIProcessedDataDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**survey_id** | **int** | The Id of the Survey | [optional] 
**start_date** | **datetime** | The Id of the Survey status | [optional] 
**end_date** | **datetime** |  | [optional] 
**market_id** | **int** |  | [optional] 
**market_name** | **str** |  | [optional] 
**market_latitude** | **float** |  | [optional] 
**market_longitude** | **float** |  | [optional] 
**regional_bureau_id** | **int** |  | [optional] 
**regional_bureau_name** | **str** |  | [optional] 
**adm0_code** | **int** |  | [optional] 
**adm0_name** | **str** |  | [optional] 
**adm1_code** | **int** |  | [optional] 
**adm1_name** | **str** |  | [optional] 
**adm2_code** | **int** |  | [optional] 
**adm2_name** | **str** |  | [optional] 
**level_id** | **int** |  | [optional] 
**level_name** | **str** |  | [optional] 
**dimension_id** | **int** |  | [optional] 
**dimension_name** | **str** |  | [optional] 
**variable_id** | **int** |  | [optional] 
**variable_name** | **str** |  | [optional] 
**variable_label** | **str** |  | [optional] 
**output_value** | **float** |  | [optional] 
**traders_sample_size** | **int** |  | [optional] 
**base_xls_form_id** | **int** |  | [optional] 
**base_xls_form_name** | **str** |  | [optional] 

## Example

```python
from data_bridges_client.models.mfi_processed_data_dto import MFIProcessedDataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MFIProcessedDataDTO from a JSON string
mfi_processed_data_dto_instance = MFIProcessedDataDTO.from_json(json)
# print the JSON string representation of the object
print MFIProcessedDataDTO.to_json()

# convert the object into a dict
mfi_processed_data_dto_dict = mfi_processed_data_dto_instance.to_dict()
# create an instance of MFIProcessedDataDTO from a dict
mfi_processed_data_dto_form_dict = mfi_processed_data_dto.from_dict(mfi_processed_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


