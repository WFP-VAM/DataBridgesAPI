# coding: utf-8

"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

    The version of the OpenAPI document: 2.0.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from data_bridges_client.models.view_extended_aggregated_price import ViewExtendedAggregatedPrice

class TestViewExtendedAggregatedPrice(unittest.TestCase):
    """ViewExtendedAggregatedPrice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ViewExtendedAggregatedPrice:
        """Test ViewExtendedAggregatedPrice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ViewExtendedAggregatedPrice`
        """
        model = ViewExtendedAggregatedPrice()
        if include_optional:
            return ViewExtendedAggregatedPrice(
                commodity_id = 56,
                market_id = 56,
                price_type_id = 56,
                commodity_unit_id = 56,
                currency_id = 56,
                adm0_code = 56,
                commodity_date_week = 56,
                commodity_date_month = 56,
                commodity_date_year = 56,
                commodity_price_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                commodity_name = '',
                market_name = '',
                price_type_name = '',
                commodity_unit_name = '',
                currency_name = '',
                country_iso3 = '',
                country_name = '',
                commodity_price_source_name = '',
                original_frequency = '',
                commodity_price = 1.337,
                commodity_price_observations = 56,
                commodity_price_flag = ''
            )
        else:
            return ViewExtendedAggregatedPrice(
        )
        """

    def testViewExtendedAggregatedPrice(self):
        """Test ViewExtendedAggregatedPrice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
