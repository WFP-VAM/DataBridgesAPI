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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from data_bridges_client.models.xls_form_fields_dto import XlsFormFieldsDTO
from typing import Optional, Set
from typing_extensions import Self

class XlsFormDefinitionNewSchemaDTO(BaseModel):
    """
    XlsFormDefinitionNewSchemaDTO
    """ # noqa: E501
    form_name: Optional[StrictStr] = Field(default=None, alias="formName")
    form_description: Optional[StrictStr] = Field(default=None, alias="formDescription")
    form_type: Optional[StrictStr] = Field(default=None, alias="formType")
    adm0_code: Optional[StrictInt] = Field(default=None, alias="adm0Code")
    base_schema_id: Optional[StrictInt] = Field(default=None, alias="baseSchemaId")
    category: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    fields: Optional[List[XlsFormFieldsDTO]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["formName", "formDescription", "formType", "adm0Code", "baseSchemaId", "category", "type", "fields"]

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
        """Create an instance of XlsFormDefinitionNewSchemaDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item_fields in self.fields:
                if _item_fields:
                    _items.append(_item_fields.to_dict())
            _dict['fields'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if form_name (nullable) is None
        # and model_fields_set contains the field
        if self.form_name is None and "form_name" in self.model_fields_set:
            _dict['formName'] = None

        # set to None if form_description (nullable) is None
        # and model_fields_set contains the field
        if self.form_description is None and "form_description" in self.model_fields_set:
            _dict['formDescription'] = None

        # set to None if form_type (nullable) is None
        # and model_fields_set contains the field
        if self.form_type is None and "form_type" in self.model_fields_set:
            _dict['formType'] = None

        # set to None if adm0_code (nullable) is None
        # and model_fields_set contains the field
        if self.adm0_code is None and "adm0_code" in self.model_fields_set:
            _dict['adm0Code'] = None

        # set to None if base_schema_id (nullable) is None
        # and model_fields_set contains the field
        if self.base_schema_id is None and "base_schema_id" in self.model_fields_set:
            _dict['baseSchemaId'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if fields (nullable) is None
        # and model_fields_set contains the field
        if self.fields is None and "fields" in self.model_fields_set:
            _dict['fields'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of XlsFormDefinitionNewSchemaDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "formName": obj.get("formName"),
            "formDescription": obj.get("formDescription"),
            "formType": obj.get("formType"),
            "adm0Code": obj.get("adm0Code"),
            "baseSchemaId": obj.get("baseSchemaId"),
            "category": obj.get("category"),
            "type": obj.get("type"),
            "fields": [XlsFormFieldsDTO.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


