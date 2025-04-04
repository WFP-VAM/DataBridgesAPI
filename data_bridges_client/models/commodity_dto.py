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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from data_bridges_client.models.commodity_processing_dto import CommodityProcessingDTO
from data_bridges_client.models.commodity_quality_dto import CommodityQualityDTO
from typing import Optional, Set
from typing_extensions import Self

class CommodityDTO(BaseModel):
    """
    CommodityDTO
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The internal ID of the commodity")
    parent_id: Optional[StrictInt] = Field(default=None, description="The internal parent ID of the commodity", alias="parentId")
    name: Optional[StrictStr] = Field(default=None, description="The name of the commodity")
    coicop2018: Optional[StrictStr] = Field(default=None, description="The COICOP 2018 definition")
    supply: Optional[StrictInt] = None
    category_id: Optional[StrictInt] = Field(default=None, alias="categoryId")
    create_date: Optional[datetime] = Field(default=None, alias="createDate")
    update_date: Optional[datetime] = Field(default=None, alias="updateDate")
    qualities: Optional[List[CommodityQualityDTO]] = None
    processing: Optional[List[CommodityProcessingDTO]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "parentId", "name", "coicop2018", "supply", "categoryId", "createDate", "updateDate", "qualities", "processing"]

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
        """Create an instance of CommodityDTO from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in qualities (list)
        _items = []
        if self.qualities:
            for _item_qualities in self.qualities:
                if _item_qualities:
                    _items.append(_item_qualities.to_dict())
            _dict['qualities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in processing (list)
        _items = []
        if self.processing:
            for _item_processing in self.processing:
                if _item_processing:
                    _items.append(_item_processing.to_dict())
            _dict['processing'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_id is None and "parent_id" in self.model_fields_set:
            _dict['parentId'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if coicop2018 (nullable) is None
        # and model_fields_set contains the field
        if self.coicop2018 is None and "coicop2018" in self.model_fields_set:
            _dict['coicop2018'] = None

        # set to None if supply (nullable) is None
        # and model_fields_set contains the field
        if self.supply is None and "supply" in self.model_fields_set:
            _dict['supply'] = None

        # set to None if update_date (nullable) is None
        # and model_fields_set contains the field
        if self.update_date is None and "update_date" in self.model_fields_set:
            _dict['updateDate'] = None

        # set to None if qualities (nullable) is None
        # and model_fields_set contains the field
        if self.qualities is None and "qualities" in self.model_fields_set:
            _dict['qualities'] = None

        # set to None if processing (nullable) is None
        # and model_fields_set contains the field
        if self.processing is None and "processing" in self.model_fields_set:
            _dict['processing'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommodityDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "parentId": obj.get("parentId"),
            "name": obj.get("name"),
            "coicop2018": obj.get("coicop2018"),
            "supply": obj.get("supply"),
            "categoryId": obj.get("categoryId"),
            "createDate": obj.get("createDate"),
            "updateDate": obj.get("updateDate"),
            "qualities": [CommodityQualityDTO.from_dict(_item) for _item in obj["qualities"]] if obj.get("qualities") is not None else None,
            "processing": [CommodityProcessingDTO.from_dict(_item) for _item in obj["processing"]] if obj.get("processing") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


