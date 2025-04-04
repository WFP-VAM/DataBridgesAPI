# coding: utf-8

"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

    The version of the OpenAPI document: 6.0.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from data_bridges_client.models.key_name_dto import KeyNameDto
from typing import Optional, Set
from typing_extensions import Self

class HouseholdSurveyListDTO(BaseModel):
    """
    HouseholdSurveyListDTO
    """ # noqa: E501
    survey_id: Optional[StrictInt] = Field(default=None, description="The Id of the Survey", alias="surveyID")
    survey_status_id: Optional[StrictInt] = Field(default=None, description="The Id of the Survey status", alias="surveyStatusID")
    survey_start_date: Optional[datetime] = Field(default=None, description="The date when the survey has started", alias="surveyStartDate")
    survey_end_date: Optional[datetime] = Field(default=None, description="The date when the survey has ended", alias="surveyEndDate")
    survey_create_date: Optional[datetime] = Field(default=None, description="The date when the survey has been uploaded in the Data Bridges platform", alias="surveyCreateDate")
    survey_validation_report: Optional[StrictStr] = Field(default=None, description="The detailed report on the validation performed on the survey schema", alias="surveyValidationReport")
    survey_original_filename: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=256)]] = Field(default=None, description="The filename of the survey CSV file", alias="surveyOriginalFilename")
    xls_form_name: Optional[StrictStr] = Field(default=None, description="The name of the XLSForm used to collect data", alias="xlsFormName")
    base_xls_form_name: Optional[StrictStr] = Field(default=None, description="The name of the base XLSForm used to build the XLSForm", alias="baseXlsFormName")
    country_name: Optional[StrictStr] = Field(default=None, description="The name of the country where the survey has taken place", alias="countryName")
    adm0_code: Optional[StrictInt] = Field(default=None, description="The internal code of the country where the survey has taken place", alias="adm0Code")
    iso3_alpha3: Optional[StrictStr] = Field(default=None, description="The ISO3 alpha code of the country where the survey has taken place", alias="iso3Alpha3")
    user_name: Optional[StrictStr] = Field(default=None, description="The name of the user that has uploaded the survey data", alias="userName")
    approved_by: Optional[StrictStr] = Field(default=None, alias="approvedBy")
    original_csv_file: Optional[StrictStr] = Field(default=None, description="The link to download the original CSV file", alias="originalCsvFile")
    base_data: Optional[StrictStr] = Field(default=None, description="The link to the JSON data reshaped on the base XLSForm", alias="baseData")
    survey_attributes: Optional[List[KeyNameDto]] = Field(default=None, alias="surveyAttributes")
    organizations: Optional[List[KeyNameDto]] = None
    survey_modality_name: Optional[StrictStr] = Field(default=None, alias="surveyModalityName")
    survey_category_name: Optional[StrictStr] = Field(default=None, alias="surveyCategoryName")
    survey_sub_category_name: Optional[StrictStr] = Field(default=None, alias="surveySubCategoryName")
    survey_phase_name: Optional[StrictStr] = Field(default=None, alias="surveyPhaseName")
    survey_visibility: Optional[StrictStr] = Field(default=None, alias="surveyVisibility")
    is_continuous_monitoring: Optional[StrictBool] = Field(default=None, alias="isContinuousMonitoring")
    survey_name: Optional[StrictStr] = Field(default=None, alias="surveyName")
    xls_form_id: Optional[StrictInt] = Field(default=None, alias="xlsFormId")
    base_xls_form_id: Optional[StrictInt] = Field(default=None, alias="baseXlsFormId")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["surveyID", "surveyStatusID", "surveyStartDate", "surveyEndDate", "surveyCreateDate", "surveyValidationReport", "surveyOriginalFilename", "xlsFormName", "baseXlsFormName", "countryName", "adm0Code", "iso3Alpha3", "userName", "approvedBy", "originalCsvFile", "baseData", "surveyAttributes", "organizations", "surveyModalityName", "surveyCategoryName", "surveySubCategoryName", "surveyPhaseName", "surveyVisibility", "isContinuousMonitoring", "surveyName", "xlsFormId", "baseXlsFormId"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of HouseholdSurveyListDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in survey_attributes (list)
        _items = []
        if self.survey_attributes:
            for _item_survey_attributes in self.survey_attributes:
                if _item_survey_attributes:
                    _items.append(_item_survey_attributes.to_dict())
            _dict['surveyAttributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in organizations (list)
        _items = []
        if self.organizations:
            for _item_organizations in self.organizations:
                if _item_organizations:
                    _items.append(_item_organizations.to_dict())
            _dict['organizations'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if survey_start_date (nullable) is None
        # and model_fields_set contains the field
        if self.survey_start_date is None and "survey_start_date" in self.model_fields_set:
            _dict['surveyStartDate'] = None

        # set to None if survey_end_date (nullable) is None
        # and model_fields_set contains the field
        if self.survey_end_date is None and "survey_end_date" in self.model_fields_set:
            _dict['surveyEndDate'] = None

        # set to None if survey_validation_report (nullable) is None
        # and model_fields_set contains the field
        if self.survey_validation_report is None and "survey_validation_report" in self.model_fields_set:
            _dict['surveyValidationReport'] = None

        # set to None if survey_original_filename (nullable) is None
        # and model_fields_set contains the field
        if self.survey_original_filename is None and "survey_original_filename" in self.model_fields_set:
            _dict['surveyOriginalFilename'] = None

        # set to None if xls_form_name (nullable) is None
        # and model_fields_set contains the field
        if self.xls_form_name is None and "xls_form_name" in self.model_fields_set:
            _dict['xlsFormName'] = None

        # set to None if base_xls_form_name (nullable) is None
        # and model_fields_set contains the field
        if self.base_xls_form_name is None and "base_xls_form_name" in self.model_fields_set:
            _dict['baseXlsFormName'] = None

        # set to None if country_name (nullable) is None
        # and model_fields_set contains the field
        if self.country_name is None and "country_name" in self.model_fields_set:
            _dict['countryName'] = None

        # set to None if iso3_alpha3 (nullable) is None
        # and model_fields_set contains the field
        if self.iso3_alpha3 is None and "iso3_alpha3" in self.model_fields_set:
            _dict['iso3Alpha3'] = None

        # set to None if user_name (nullable) is None
        # and model_fields_set contains the field
        if self.user_name is None and "user_name" in self.model_fields_set:
            _dict['userName'] = None

        # set to None if approved_by (nullable) is None
        # and model_fields_set contains the field
        if self.approved_by is None and "approved_by" in self.model_fields_set:
            _dict['approvedBy'] = None

        # set to None if original_csv_file (nullable) is None
        # and model_fields_set contains the field
        if self.original_csv_file is None and "original_csv_file" in self.model_fields_set:
            _dict['originalCsvFile'] = None

        # set to None if base_data (nullable) is None
        # and model_fields_set contains the field
        if self.base_data is None and "base_data" in self.model_fields_set:
            _dict['baseData'] = None

        # set to None if survey_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.survey_attributes is None and "survey_attributes" in self.model_fields_set:
            _dict['surveyAttributes'] = None

        # set to None if organizations (nullable) is None
        # and model_fields_set contains the field
        if self.organizations is None and "organizations" in self.model_fields_set:
            _dict['organizations'] = None

        # set to None if survey_modality_name (nullable) is None
        # and model_fields_set contains the field
        if self.survey_modality_name is None and "survey_modality_name" in self.model_fields_set:
            _dict['surveyModalityName'] = None

        # set to None if survey_category_name (nullable) is None
        # and model_fields_set contains the field
        if self.survey_category_name is None and "survey_category_name" in self.model_fields_set:
            _dict['surveyCategoryName'] = None

        # set to None if survey_sub_category_name (nullable) is None
        # and model_fields_set contains the field
        if self.survey_sub_category_name is None and "survey_sub_category_name" in self.model_fields_set:
            _dict['surveySubCategoryName'] = None

        # set to None if survey_phase_name (nullable) is None
        # and model_fields_set contains the field
        if self.survey_phase_name is None and "survey_phase_name" in self.model_fields_set:
            _dict['surveyPhaseName'] = None

        # set to None if survey_visibility (nullable) is None
        # and model_fields_set contains the field
        if self.survey_visibility is None and "survey_visibility" in self.model_fields_set:
            _dict['surveyVisibility'] = None

        # set to None if survey_name (nullable) is None
        # and model_fields_set contains the field
        if self.survey_name is None and "survey_name" in self.model_fields_set:
            _dict['surveyName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HouseholdSurveyListDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "surveyID": obj.get("surveyID"),
            "surveyStatusID": obj.get("surveyStatusID"),
            "surveyStartDate": obj.get("surveyStartDate"),
            "surveyEndDate": obj.get("surveyEndDate"),
            "surveyCreateDate": obj.get("surveyCreateDate"),
            "surveyValidationReport": obj.get("surveyValidationReport"),
            "surveyOriginalFilename": obj.get("surveyOriginalFilename"),
            "xlsFormName": obj.get("xlsFormName"),
            "baseXlsFormName": obj.get("baseXlsFormName"),
            "countryName": obj.get("countryName"),
            "adm0Code": obj.get("adm0Code"),
            "iso3Alpha3": obj.get("iso3Alpha3"),
            "userName": obj.get("userName"),
            "approvedBy": obj.get("approvedBy"),
            "originalCsvFile": obj.get("originalCsvFile"),
            "baseData": obj.get("baseData"),
            "surveyAttributes": [KeyNameDto.from_dict(_item) for _item in obj["surveyAttributes"]] if obj.get("surveyAttributes") is not None else None,
            "organizations": [KeyNameDto.from_dict(_item) for _item in obj["organizations"]] if obj.get("organizations") is not None else None,
            "surveyModalityName": obj.get("surveyModalityName"),
            "surveyCategoryName": obj.get("surveyCategoryName"),
            "surveySubCategoryName": obj.get("surveySubCategoryName"),
            "surveyPhaseName": obj.get("surveyPhaseName"),
            "surveyVisibility": obj.get("surveyVisibility"),
            "isContinuousMonitoring": obj.get("isContinuousMonitoring"),
            "surveyName": obj.get("surveyName"),
            "xlsFormId": obj.get("xlsFormId"),
            "baseXlsFormId": obj.get("baseXlsFormId")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


