# coding: utf-8

"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

    The version of the OpenAPI document: 4.1.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class UsdIndirectQuotation(BaseModel):
    """
    UsdIndirectQuotation
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: Optional[StrictStr] = Field(default=None, description="the ISO3 code for the currency, based on ISO4217")
    adm0_code: Optional[StrictInt] = Field(default=None, alias="adm0Code")
    country_iso3: Optional[StrictStr] = Field(default=None, alias="countryISO3")
    is_official: Optional[StrictBool] = Field(default=None, description="The field IsOfficial is a boolean which can be set to true for the Trading Economics data and to false for the data coming from a commodity saved in the DataBridges database", alias="isOfficial")
    frequency: Optional[StrictStr] = Field(default=None, description="(it’s from the reporting commodity named Exchange Rate")
    value: Optional[Union[StrictFloat, StrictInt]] = None
    var_date: Optional[datetime] = Field(default=None, alias="date")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "name", "adm0Code", "countryISO3", "isOfficial", "frequency", "value", "date"]

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
        """Create an instance of UsdIndirectQuotation from a JSON string"""
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

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if country_iso3 (nullable) is None
        # and model_fields_set contains the field
        if self.country_iso3 is None and "country_iso3" in self.model_fields_set:
            _dict['countryISO3'] = None

        # set to None if frequency (nullable) is None
        # and model_fields_set contains the field
        if self.frequency is None and "frequency" in self.model_fields_set:
            _dict['frequency'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsdIndirectQuotation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "adm0Code": obj.get("adm0Code"),
            "countryISO3": obj.get("countryISO3"),
            "isOfficial": obj.get("isOfficial"),
            "frequency": obj.get("frequency"),
            "value": obj.get("value"),
            "date": obj.get("date")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


