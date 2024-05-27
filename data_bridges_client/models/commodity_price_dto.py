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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CommodityPriceDTO(BaseModel):
    """
    CommodityPriceDTO
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The internal ID of the commodity")
    commodity_id: Optional[StrictInt] = Field(default=None, alias="commodityId")
    market_id: Optional[StrictInt] = Field(default=None, alias="marketId")
    price_type_id: Optional[StrictInt] = Field(default=None, alias="priceTypeId")
    commodity_unit_id: Optional[StrictInt] = Field(default=None, alias="commodityUnitId")
    currency_id: Optional[StrictInt] = Field(default=None, alias="currencyId")
    commodity_name: Optional[StrictStr] = Field(default=None, alias="commodityName")
    market_name: Optional[StrictStr] = Field(default=None, alias="marketName")
    price_type_name: Optional[StrictStr] = Field(default=None, alias="priceTypeName")
    unit_name: Optional[StrictStr] = Field(default=None, alias="unitName")
    currency_name: Optional[StrictStr] = Field(default=None, alias="currencyName")
    original_frequency: Optional[StrictStr] = Field(default=None, alias="originalFrequency")
    adm0_code: Optional[StrictInt] = Field(default=None, alias="adm0Code")
    country_iso3: Optional[StrictStr] = Field(default=None, alias="countryISO3")
    country_name: Optional[StrictStr] = Field(default=None, alias="countryName")
    commodity_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="commodityPrice")
    commodity_price_source_name: Optional[StrictStr] = Field(default=None, alias="commodityPriceSourceName")
    commodity_price_metadata: Optional[Any] = Field(default=None, alias="commodityPriceMetadata")
    commodity_price_date: Optional[datetime] = Field(default=None, alias="commodityPriceDate")
    commodity_price_observations: Optional[StrictInt] = Field(default=None, alias="commodityPriceObservations")
    commodity_price_date_day: Optional[StrictInt] = Field(default=None, alias="commodityPriceDateDay")
    commodity_price_date_week: Optional[StrictInt] = Field(default=None, alias="commodityPriceDateWeek")
    commodity_price_date_month: Optional[StrictInt] = Field(default=None, alias="commodityPriceDateMonth")
    commodity_price_date_year: Optional[StrictInt] = Field(default=None, alias="commodityPriceDateYear")
    commodity_price_insert_date: Optional[datetime] = Field(default=None, alias="commodityPriceInsertDate")
    commodity_price_flag: Optional[StrictStr] = Field(default=None, alias="commodityPriceFlag")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "commodityId", "marketId", "priceTypeId", "commodityUnitId", "currencyId", "commodityName", "marketName", "priceTypeName", "unitName", "currencyName", "originalFrequency", "adm0Code", "countryISO3", "countryName", "commodityPrice", "commodityPriceSourceName", "commodityPriceMetadata", "commodityPriceDate", "commodityPriceObservations", "commodityPriceDateDay", "commodityPriceDateWeek", "commodityPriceDateMonth", "commodityPriceDateYear", "commodityPriceInsertDate", "commodityPriceFlag"]

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
        """Create an instance of CommodityPriceDTO from a JSON string"""
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

        # set to None if commodity_name (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_name is None and "commodity_name" in self.model_fields_set:
            _dict['commodityName'] = None

        # set to None if market_name (nullable) is None
        # and model_fields_set contains the field
        if self.market_name is None and "market_name" in self.model_fields_set:
            _dict['marketName'] = None

        # set to None if price_type_name (nullable) is None
        # and model_fields_set contains the field
        if self.price_type_name is None and "price_type_name" in self.model_fields_set:
            _dict['priceTypeName'] = None

        # set to None if unit_name (nullable) is None
        # and model_fields_set contains the field
        if self.unit_name is None and "unit_name" in self.model_fields_set:
            _dict['unitName'] = None

        # set to None if currency_name (nullable) is None
        # and model_fields_set contains the field
        if self.currency_name is None and "currency_name" in self.model_fields_set:
            _dict['currencyName'] = None

        # set to None if original_frequency (nullable) is None
        # and model_fields_set contains the field
        if self.original_frequency is None and "original_frequency" in self.model_fields_set:
            _dict['originalFrequency'] = None

        # set to None if country_iso3 (nullable) is None
        # and model_fields_set contains the field
        if self.country_iso3 is None and "country_iso3" in self.model_fields_set:
            _dict['countryISO3'] = None

        # set to None if country_name (nullable) is None
        # and model_fields_set contains the field
        if self.country_name is None and "country_name" in self.model_fields_set:
            _dict['countryName'] = None

        # set to None if commodity_price_source_name (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_price_source_name is None and "commodity_price_source_name" in self.model_fields_set:
            _dict['commodityPriceSourceName'] = None

        # set to None if commodity_price_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_price_metadata is None and "commodity_price_metadata" in self.model_fields_set:
            _dict['commodityPriceMetadata'] = None

        # set to None if commodity_price_observations (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_price_observations is None and "commodity_price_observations" in self.model_fields_set:
            _dict['commodityPriceObservations'] = None

        # set to None if commodity_price_date_day (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_price_date_day is None and "commodity_price_date_day" in self.model_fields_set:
            _dict['commodityPriceDateDay'] = None

        # set to None if commodity_price_date_week (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_price_date_week is None and "commodity_price_date_week" in self.model_fields_set:
            _dict['commodityPriceDateWeek'] = None

        # set to None if commodity_price_date_month (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_price_date_month is None and "commodity_price_date_month" in self.model_fields_set:
            _dict['commodityPriceDateMonth'] = None

        # set to None if commodity_price_insert_date (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_price_insert_date is None and "commodity_price_insert_date" in self.model_fields_set:
            _dict['commodityPriceInsertDate'] = None

        # set to None if commodity_price_flag (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_price_flag is None and "commodity_price_flag" in self.model_fields_set:
            _dict['commodityPriceFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommodityPriceDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "commodityId": obj.get("commodityId"),
            "marketId": obj.get("marketId"),
            "priceTypeId": obj.get("priceTypeId"),
            "commodityUnitId": obj.get("commodityUnitId"),
            "currencyId": obj.get("currencyId"),
            "commodityName": obj.get("commodityName"),
            "marketName": obj.get("marketName"),
            "priceTypeName": obj.get("priceTypeName"),
            "unitName": obj.get("unitName"),
            "currencyName": obj.get("currencyName"),
            "originalFrequency": obj.get("originalFrequency"),
            "adm0Code": obj.get("adm0Code"),
            "countryISO3": obj.get("countryISO3"),
            "countryName": obj.get("countryName"),
            "commodityPrice": obj.get("commodityPrice"),
            "commodityPriceSourceName": obj.get("commodityPriceSourceName"),
            "commodityPriceMetadata": obj.get("commodityPriceMetadata"),
            "commodityPriceDate": obj.get("commodityPriceDate"),
            "commodityPriceObservations": obj.get("commodityPriceObservations"),
            "commodityPriceDateDay": obj.get("commodityPriceDateDay"),
            "commodityPriceDateWeek": obj.get("commodityPriceDateWeek"),
            "commodityPriceDateMonth": obj.get("commodityPriceDateMonth"),
            "commodityPriceDateYear": obj.get("commodityPriceDateYear"),
            "commodityPriceInsertDate": obj.get("commodityPriceInsertDate"),
            "commodityPriceFlag": obj.get("commodityPriceFlag")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


