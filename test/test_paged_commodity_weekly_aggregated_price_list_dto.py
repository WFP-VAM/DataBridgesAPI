"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import data_bridges_client
from data_bridges_client.model.weekly_aggregated_price import WeeklyAggregatedPrice
globals()['WeeklyAggregatedPrice'] = WeeklyAggregatedPrice
from data_bridges_client.model.paged_commodity_weekly_aggregated_price_list_dto import PagedCommodityWeeklyAggregatedPriceListDTO


class TestPagedCommodityWeeklyAggregatedPriceListDTO(unittest.TestCase):
    """PagedCommodityWeeklyAggregatedPriceListDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPagedCommodityWeeklyAggregatedPriceListDTO(self):
        """Test PagedCommodityWeeklyAggregatedPriceListDTO"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PagedCommodityWeeklyAggregatedPriceListDTO()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
