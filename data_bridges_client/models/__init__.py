# coding: utf-8

# flake8: noqa
"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

    The version of the OpenAPI document: 2.0.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from data_bridges_client.models.bad_request_dto import BadRequestDTO
from data_bridges_client.models.commodity_dto import CommodityDTO
from data_bridges_client.models.commodity_price_dto import CommodityPriceDTO
from data_bridges_client.models.commodity_processing_dto import CommodityProcessingDTO
from data_bridges_client.models.commodity_quality_dto import CommodityQualityDTO
from data_bridges_client.models.currency_dto import CurrencyDTO
from data_bridges_client.models.economic_data_dto import EconomicDataDTO
from data_bridges_client.models.economic_indicator_property import EconomicIndicatorProperty
from data_bridges_client.models.economic_indicator_property_paged_result import EconomicIndicatorPropertyPagedResult
from data_bridges_client.models.feature import Feature
from data_bridges_client.models.geometry import Geometry
from data_bridges_client.models.gorp_value_with_changes import GorpValueWithChanges
from data_bridges_client.models.gorp_value_with_changes_paged_result import GorpValueWithChangesPagedResult
from data_bridges_client.models.household_survey_list_dto import HouseholdSurveyListDTO
from data_bridges_client.models.household_survey_list_dto_paged_result import HouseholdSurveyListDTOPagedResult
from data_bridges_client.models.ipc_value import IpcValue
from data_bridges_client.models.ipc_value_paged_result import IpcValuePagedResult
from data_bridges_client.models.key_name_dto import KeyNameDto
from data_bridges_client.models.mfi_processed_data_dto import MFIProcessedDataDTO
from data_bridges_client.models.market_dto import MarketDTO
from data_bridges_client.models.market_geo_json_root import MarketGeoJsonRoot
from data_bridges_client.models.nearby_markets_dto import NearbyMarketsDTO
from data_bridges_client.models.paged_commodity_list_dto import PagedCommodityListDTO
from data_bridges_client.models.paged_commodity_price_list_dto import PagedCommodityPriceListDTO
from data_bridges_client.models.paged_commodity_weekly_aggregated_price_list_dto import PagedCommodityWeeklyAggregatedPriceListDTO
from data_bridges_client.models.paged_currency_list_dto import PagedCurrencyListDTO
from data_bridges_client.models.paged_economic_data_dto import PagedEconomicDataDTO
from data_bridges_client.models.paged_market_list_dto import PagedMarketListDTO
from data_bridges_client.models.paged_processed_data_dto import PagedProcessedDataDTO
from data_bridges_client.models.paged_survey_list_dto import PagedSurveyListDTO
from data_bridges_client.models.paged_survey_responses_dto import PagedSurveyResponsesDTO
from data_bridges_client.models.paged_xls_form_list_dto import PagedXlsFormListDTO
from data_bridges_client.models.problem_details import ProblemDetails
from data_bridges_client.models.properties import Properties
from data_bridges_client.models.rpme_assessment import RpmeAssessment
from data_bridges_client.models.rpme_assessment_paged_result import RpmeAssessmentPagedResult
from data_bridges_client.models.rpme_output_values import RpmeOutputValues
from data_bridges_client.models.rpme_variable import RpmeVariable
from data_bridges_client.models.rpme_variable_paged_result import RpmeVariablePagedResult
from data_bridges_client.models.survey_list_dto import SurveyListDTO
from data_bridges_client.models.usd_indirect_quotation import UsdIndirectQuotation
from data_bridges_client.models.usd_indirect_quotation_paged_result import UsdIndirectQuotationPagedResult
from data_bridges_client.models.view_extended_aggregated_price import ViewExtendedAggregatedPrice
from data_bridges_client.models.view_extended_aggregated_price_paged_result import ViewExtendedAggregatedPricePagedResult
from data_bridges_client.models.view_extended_alps_value import ViewExtendedAlpsValue
from data_bridges_client.models.view_extended_alps_value_paged_result import ViewExtendedAlpsValuePagedResult
from data_bridges_client.models.weekly_aggregated_price import WeeklyAggregatedPrice
from data_bridges_client.models.xls_form_dto import XlsFormDTO
from data_bridges_client.models.xls_form_definition_dto import XlsFormDefinitionDTO
