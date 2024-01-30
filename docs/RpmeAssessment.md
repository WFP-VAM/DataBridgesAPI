# RpmeAssessment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**survey_id** | **int** |  | [optional] 
**assessment_date** | **datetime** |  | [optional] 
**shop_id** | **int** |  | [optional] 
**adm0_code** | **int** |  | [optional] 
**adm1_code** | **int** |  | [optional] 
**adm2_code** | **int** |  | [optional] 
**adm0_code_dots** | **str** |  | [optional] 
**adm1_code_dots** | **str** |  | [optional] 
**adm2_code_dots** | **str** |  | [optional] 
**market_id** | **int** |  | [optional] 
**sh_latitude** | **float** |  | [optional] 
**sh_longitude** | **float** |  | [optional] 
**nb_beneficiaries_interviewed** | **int** |  | [optional] 
**price_score_tbu** | **bool** |  | [optional] 
**price_score_tbd** | **bool** |  | [optional] 
**beneficiaries_score_tbu** | **bool** |  | [optional] 
**trd_name** | **str** |  | [optional] 
**sev_cntr_dev** | **str** |  | [optional] 
**ben_sev_cntr_dev** | **str** |  | [optional] 
**output_values** | [**List[RpmeOutputValues]**](RpmeOutputValues.md) |  | [optional] 

## Example

```python
from data_bridges_client.models.rpme_assessment import RpmeAssessment

# TODO update the JSON string below
json = "{}"
# create an instance of RpmeAssessment from a JSON string
rpme_assessment_instance = RpmeAssessment.from_json(json)
# print the JSON string representation of the object
print RpmeAssessment.to_json()

# convert the object into a dict
rpme_assessment_dict = rpme_assessment_instance.to_dict()
# create an instance of RpmeAssessment from a dict
rpme_assessment_form_dict = rpme_assessment.from_dict(rpme_assessment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


