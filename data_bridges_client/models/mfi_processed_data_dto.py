# coding: utf-8

"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

    The version of the OpenAPI document: 5.0.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class MFIProcessedDataDTO(BaseModel):
    """
    MFIProcessedDataDTO
    """ # noqa: E501
    survey_id: Optional[StrictInt] = Field(default=None, description="The Id of the Survey", alias="surveyID")
    start_date: Optional[datetime] = Field(default=None, description="The Id of the Survey status", alias="startDate")
    end_date: Optional[datetime] = Field(default=None, alias="endDate")
    market_id: Optional[StrictInt] = Field(default=None, alias="marketID")
    market_name: Optional[StrictStr] = Field(default=None, alias="marketName")
    market_latitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="marketLatitude")
    market_longitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="marketLongitude")
    regional_bureau_id: Optional[StrictInt] = Field(default=None, alias="regionalBureauID")
    regional_bureau_name: Optional[StrictStr] = Field(default=None, alias="regionalBureauName")
    adm0_code: Optional[StrictInt] = Field(default=None, alias="adm0Code")
    adm0_name: Optional[StrictStr] = Field(default=None, alias="adm0Name")
    adm1_code: Optional[StrictInt] = Field(default=None, alias="adm1Code")
    adm1_name: Optional[StrictStr] = Field(default=None, alias="adm1Name")
    adm2_code: Optional[StrictInt] = Field(default=None, alias="adm2Code")
    adm2_name: Optional[StrictStr] = Field(default=None, alias="adm2Name")
    level_id: Optional[StrictInt] = Field(default=None, alias="levelID")
    level_name: Optional[StrictStr] = Field(default=None, alias="levelName")
    dimension_id: Optional[StrictInt] = Field(default=None, alias="dimensionID")
    dimension_name: Optional[StrictStr] = Field(default=None, alias="dimensionName")
    variable_id: Optional[StrictInt] = Field(default=None, alias="variableID")
    variable_name: Optional[StrictStr] = Field(default=None, alias="variableName")
    variable_label: Optional[StrictStr] = Field(default=None, alias="variableLabel")
    output_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="outputValue")
    traders_sample_size: Optional[StrictInt] = Field(default=None, alias="tradersSampleSize")
    base_xls_form_id: Optional[StrictInt] = Field(default=None, alias="baseXlsFormID")
    base_xls_form_name: Optional[StrictStr] = Field(default=None, alias="baseXlsFormName")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["surveyID", "startDate", "endDate", "marketID", "marketName", "marketLatitude", "marketLongitude", "regionalBureauID", "regionalBureauName", "adm0Code", "adm0Name", "adm1Code", "adm1Name", "adm2Code", "adm2Name", "levelID", "levelName", "dimensionID", "dimensionName", "variableID", "variableName", "variableLabel", "outputValue", "tradersSampleSize", "baseXlsFormID", "baseXlsFormName"]

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
        """Create an instance of MFIProcessedDataDTO from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['startDate'] = None

        # set to None if end_date (nullable) is None
        # and model_fields_set contains the field
        if self.end_date is None and "end_date" in self.model_fields_set:
            _dict['endDate'] = None

        # set to None if market_name (nullable) is None
        # and model_fields_set contains the field
        if self.market_name is None and "market_name" in self.model_fields_set:
            _dict['marketName'] = None

        # set to None if market_latitude (nullable) is None
        # and model_fields_set contains the field
        if self.market_latitude is None and "market_latitude" in self.model_fields_set:
            _dict['marketLatitude'] = None

        # set to None if market_longitude (nullable) is None
        # and model_fields_set contains the field
        if self.market_longitude is None and "market_longitude" in self.model_fields_set:
            _dict['marketLongitude'] = None

        # set to None if regional_bureau_name (nullable) is None
        # and model_fields_set contains the field
        if self.regional_bureau_name is None and "regional_bureau_name" in self.model_fields_set:
            _dict['regionalBureauName'] = None

        # set to None if adm0_name (nullable) is None
        # and model_fields_set contains the field
        if self.adm0_name is None and "adm0_name" in self.model_fields_set:
            _dict['adm0Name'] = None

        # set to None if adm1_name (nullable) is None
        # and model_fields_set contains the field
        if self.adm1_name is None and "adm1_name" in self.model_fields_set:
            _dict['adm1Name'] = None

        # set to None if adm2_name (nullable) is None
        # and model_fields_set contains the field
        if self.adm2_name is None and "adm2_name" in self.model_fields_set:
            _dict['adm2Name'] = None

        # set to None if level_name (nullable) is None
        # and model_fields_set contains the field
        if self.level_name is None and "level_name" in self.model_fields_set:
            _dict['levelName'] = None

        # set to None if dimension_name (nullable) is None
        # and model_fields_set contains the field
        if self.dimension_name is None and "dimension_name" in self.model_fields_set:
            _dict['dimensionName'] = None

        # set to None if variable_name (nullable) is None
        # and model_fields_set contains the field
        if self.variable_name is None and "variable_name" in self.model_fields_set:
            _dict['variableName'] = None

        # set to None if variable_label (nullable) is None
        # and model_fields_set contains the field
        if self.variable_label is None and "variable_label" in self.model_fields_set:
            _dict['variableLabel'] = None

        # set to None if output_value (nullable) is None
        # and model_fields_set contains the field
        if self.output_value is None and "output_value" in self.model_fields_set:
            _dict['outputValue'] = None

        # set to None if traders_sample_size (nullable) is None
        # and model_fields_set contains the field
        if self.traders_sample_size is None and "traders_sample_size" in self.model_fields_set:
            _dict['tradersSampleSize'] = None

        # set to None if base_xls_form_name (nullable) is None
        # and model_fields_set contains the field
        if self.base_xls_form_name is None and "base_xls_form_name" in self.model_fields_set:
            _dict['baseXlsFormName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MFIProcessedDataDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "surveyID": obj.get("surveyID"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "marketID": obj.get("marketID"),
            "marketName": obj.get("marketName"),
            "marketLatitude": obj.get("marketLatitude"),
            "marketLongitude": obj.get("marketLongitude"),
            "regionalBureauID": obj.get("regionalBureauID"),
            "regionalBureauName": obj.get("regionalBureauName"),
            "adm0Code": obj.get("adm0Code"),
            "adm0Name": obj.get("adm0Name"),
            "adm1Code": obj.get("adm1Code"),
            "adm1Name": obj.get("adm1Name"),
            "adm2Code": obj.get("adm2Code"),
            "adm2Name": obj.get("adm2Name"),
            "levelID": obj.get("levelID"),
            "levelName": obj.get("levelName"),
            "dimensionID": obj.get("dimensionID"),
            "dimensionName": obj.get("dimensionName"),
            "variableID": obj.get("variableID"),
            "variableName": obj.get("variableName"),
            "variableLabel": obj.get("variableLabel"),
            "outputValue": obj.get("outputValue"),
            "tradersSampleSize": obj.get("tradersSampleSize"),
            "baseXlsFormID": obj.get("baseXlsFormID"),
            "baseXlsFormName": obj.get("baseXlsFormName")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


