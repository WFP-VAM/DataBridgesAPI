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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class GorpRegionalApiDto(BaseModel):
    """
    GorpRegionalApiDto
    """ # noqa: E501
    gorp_date: Optional[StrictStr] = Field(default=None, alias="gorpDate")
    gorp_region_name: Optional[StrictStr] = Field(default=None, alias="gorpRegionName")
    gorp_total_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="gorpTotalValue")
    number_of_countries: Optional[StrictInt] = Field(default=None, alias="numberOfCountries")
    gorp_comment: Optional[StrictStr] = Field(default=None, alias="gorpComment")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["gorpDate", "gorpRegionName", "gorpTotalValue", "numberOfCountries", "gorpComment"]

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
        """Create an instance of GorpRegionalApiDto from a JSON string"""
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

        # set to None if gorp_date (nullable) is None
        # and model_fields_set contains the field
        if self.gorp_date is None and "gorp_date" in self.model_fields_set:
            _dict['gorpDate'] = None

        # set to None if gorp_region_name (nullable) is None
        # and model_fields_set contains the field
        if self.gorp_region_name is None and "gorp_region_name" in self.model_fields_set:
            _dict['gorpRegionName'] = None

        # set to None if number_of_countries (nullable) is None
        # and model_fields_set contains the field
        if self.number_of_countries is None and "number_of_countries" in self.model_fields_set:
            _dict['numberOfCountries'] = None

        # set to None if gorp_comment (nullable) is None
        # and model_fields_set contains the field
        if self.gorp_comment is None and "gorp_comment" in self.model_fields_set:
            _dict['gorpComment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GorpRegionalApiDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gorpDate": obj.get("gorpDate"),
            "gorpRegionName": obj.get("gorpRegionName"),
            "gorpTotalValue": obj.get("gorpTotalValue"),
            "numberOfCountries": obj.get("numberOfCountries"),
            "gorpComment": obj.get("gorpComment")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


