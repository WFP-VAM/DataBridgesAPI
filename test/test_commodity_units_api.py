# coding: utf-8

"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

    The version of the OpenAPI document: 6.0.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from data_bridges_client.api.commodity_units_api import CommodityUnitsApi


class TestCommodityUnitsApi(unittest.TestCase):
    """CommodityUnitsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CommodityUnitsApi()

    def tearDown(self) -> None:
        pass

    def test_commodity_units_conversion_list_get(self) -> None:
        """Test case for commodity_units_conversion_list_get

        Provides conversion factors to Kilogram or Litres for each convertible unit of measure.
        """
        pass

    def test_commodity_units_list_get(self) -> None:
        """Test case for commodity_units_list_get

        Provides the detailed list of the unit of measure available in DataBridges platform
        """
        pass


if __name__ == '__main__':
    unittest.main()
