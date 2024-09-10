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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class MarketDTO(BaseModel):
    """
    MarketDTO
    """ # noqa: E501
    market_id: Optional[StrictInt] = Field(default=None, description="The internal ID of the market", alias="marketId")
    market_name: Optional[StrictStr] = Field(default=None, description="The name of the market", alias="marketName")
    market_local_name: Optional[StrictStr] = Field(default=None, description="The local name of the market", alias="marketLocalName")
    market_latitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The decimal latitude", alias="marketLatitude")
    market_longitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The decimal longitude", alias="marketLongitude")
    admin1_name: Optional[StrictStr] = Field(default=None, description="The name of the first level administrative division where the market is placed", alias="admin1Name")
    admin1_code: Optional[StrictInt] = Field(default=None, description="The code of the first level administrative division where the market is placed", alias="admin1Code")
    admin2_name: Optional[StrictStr] = Field(default=None, description="The name of the second level administrative division where the market is placed", alias="admin2Name")
    admin2_code: Optional[StrictInt] = Field(default=None, description="The code of the second level administrative division where the market is placed", alias="admin2Code")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["marketId", "marketName", "marketLocalName", "marketLatitude", "marketLongitude", "admin1Name", "admin1Code", "admin2Name", "admin2Code"]

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
        """Create an instance of MarketDTO from a JSON string"""
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

        # set to None if market_name (nullable) is None
        # and model_fields_set contains the field
        if self.market_name is None and "market_name" in self.model_fields_set:
            _dict['marketName'] = None

        # set to None if market_local_name (nullable) is None
        # and model_fields_set contains the field
        if self.market_local_name is None and "market_local_name" in self.model_fields_set:
            _dict['marketLocalName'] = None

        # set to None if market_latitude (nullable) is None
        # and model_fields_set contains the field
        if self.market_latitude is None and "market_latitude" in self.model_fields_set:
            _dict['marketLatitude'] = None

        # set to None if market_longitude (nullable) is None
        # and model_fields_set contains the field
        if self.market_longitude is None and "market_longitude" in self.model_fields_set:
            _dict['marketLongitude'] = None

        # set to None if admin1_name (nullable) is None
        # and model_fields_set contains the field
        if self.admin1_name is None and "admin1_name" in self.model_fields_set:
            _dict['admin1Name'] = None

        # set to None if admin1_code (nullable) is None
        # and model_fields_set contains the field
        if self.admin1_code is None and "admin1_code" in self.model_fields_set:
            _dict['admin1Code'] = None

        # set to None if admin2_name (nullable) is None
        # and model_fields_set contains the field
        if self.admin2_name is None and "admin2_name" in self.model_fields_set:
            _dict['admin2Name'] = None

        # set to None if admin2_code (nullable) is None
        # and model_fields_set contains the field
        if self.admin2_code is None and "admin2_code" in self.model_fields_set:
            _dict['admin2Code'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MarketDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "marketId": obj.get("marketId"),
            "marketName": obj.get("marketName"),
            "marketLocalName": obj.get("marketLocalName"),
            "marketLatitude": obj.get("marketLatitude"),
            "marketLongitude": obj.get("marketLongitude"),
            "admin1Name": obj.get("admin1Name"),
            "admin1Code": obj.get("admin1Code"),
            "admin2Name": obj.get("admin2Name"),
            "admin2Code": obj.get("admin2Code")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


