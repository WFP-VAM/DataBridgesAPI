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

class ViewExtendedAlpsValue(BaseModel):
    """
    ViewExtendedAlpsValue
    """ # noqa: E501
    commodity_id: Optional[StrictInt] = Field(default=None, alias="commodityID")
    market_id: Optional[StrictInt] = Field(default=None, alias="marketID")
    price_type_id: Optional[StrictInt] = Field(default=None, alias="priceTypeID")
    commodity_unit_id: Optional[StrictInt] = Field(default=None, alias="commodityUnitID")
    currency_id: Optional[StrictInt] = Field(default=None, alias="currencyID")
    adm0_code: Optional[StrictInt] = Field(default=None, alias="adm0Code")
    country_name: Optional[StrictStr] = Field(default=None, alias="countryName")
    commodity_price_date_year: Optional[StrictInt] = Field(default=None, alias="commodityPriceDateYear")
    commodity_price_date_month: Optional[StrictInt] = Field(default=None, alias="commodityPriceDateMonth")
    commodity_price_date_week: Optional[StrictInt] = Field(default=None, alias="commodityPriceDateWeek")
    commodity_price_date: Optional[datetime] = Field(default=None, alias="commodityPriceDate")
    commodity_name: Optional[StrictStr] = Field(default=None, alias="commodityName")
    market_name: Optional[StrictStr] = Field(default=None, alias="marketName")
    price_type_name: Optional[StrictStr] = Field(default=None, alias="priceTypeName")
    commodity_unit_name: Optional[StrictStr] = Field(default=None, alias="commodityUnitName")
    currency_name: Optional[StrictStr] = Field(default=None, alias="currencyName")
    analysis_value_estimated_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="analysisValueEstimatedPrice")
    analysis_value_pewi_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="analysisValuePewiValue")
    analysis_value_price_flag: Optional[StrictStr] = Field(default=None, alias="analysisValuePriceFlag")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["commodityID", "marketID", "priceTypeID", "commodityUnitID", "currencyID", "adm0Code", "countryName", "commodityPriceDateYear", "commodityPriceDateMonth", "commodityPriceDateWeek", "commodityPriceDate", "commodityName", "marketName", "priceTypeName", "commodityUnitName", "currencyName", "analysisValueEstimatedPrice", "analysisValuePewiValue", "analysisValuePriceFlag"]

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
        """Create an instance of ViewExtendedAlpsValue from a JSON string"""
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

        # set to None if adm0_code (nullable) is None
        # and model_fields_set contains the field
        if self.adm0_code is None and "adm0_code" in self.model_fields_set:
            _dict['adm0Code'] = None

        # set to None if country_name (nullable) is None
        # and model_fields_set contains the field
        if self.country_name is None and "country_name" in self.model_fields_set:
            _dict['countryName'] = None

        # set to None if commodity_price_date_month (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_price_date_month is None and "commodity_price_date_month" in self.model_fields_set:
            _dict['commodityPriceDateMonth'] = None

        # set to None if commodity_price_date_week (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_price_date_week is None and "commodity_price_date_week" in self.model_fields_set:
            _dict['commodityPriceDateWeek'] = None

        # set to None if commodity_price_date (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_price_date is None and "commodity_price_date" in self.model_fields_set:
            _dict['commodityPriceDate'] = None

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

        # set to None if commodity_unit_name (nullable) is None
        # and model_fields_set contains the field
        if self.commodity_unit_name is None and "commodity_unit_name" in self.model_fields_set:
            _dict['commodityUnitName'] = None

        # set to None if currency_name (nullable) is None
        # and model_fields_set contains the field
        if self.currency_name is None and "currency_name" in self.model_fields_set:
            _dict['currencyName'] = None

        # set to None if analysis_value_price_flag (nullable) is None
        # and model_fields_set contains the field
        if self.analysis_value_price_flag is None and "analysis_value_price_flag" in self.model_fields_set:
            _dict['analysisValuePriceFlag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViewExtendedAlpsValue from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "commodityID": obj.get("commodityID"),
            "marketID": obj.get("marketID"),
            "priceTypeID": obj.get("priceTypeID"),
            "commodityUnitID": obj.get("commodityUnitID"),
            "currencyID": obj.get("currencyID"),
            "adm0Code": obj.get("adm0Code"),
            "countryName": obj.get("countryName"),
            "commodityPriceDateYear": obj.get("commodityPriceDateYear"),
            "commodityPriceDateMonth": obj.get("commodityPriceDateMonth"),
            "commodityPriceDateWeek": obj.get("commodityPriceDateWeek"),
            "commodityPriceDate": obj.get("commodityPriceDate"),
            "commodityName": obj.get("commodityName"),
            "marketName": obj.get("marketName"),
            "priceTypeName": obj.get("priceTypeName"),
            "commodityUnitName": obj.get("commodityUnitName"),
            "currencyName": obj.get("currencyName"),
            "analysisValueEstimatedPrice": obj.get("analysisValueEstimatedPrice"),
            "analysisValuePewiValue": obj.get("analysisValuePewiValue"),
            "analysisValuePriceFlag": obj.get("analysisValuePriceFlag")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


