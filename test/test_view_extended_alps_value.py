# coding: utf-8

"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

<<<<<<< HEAD
    The version of the OpenAPI document: 4.1.0
=======
    The version of the OpenAPI document: 4.0.0
>>>>>>> dev
    Contact: wfp.economicanalysis@wfp.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from data_bridges_client.models.view_extended_alps_value import ViewExtendedAlpsValue

class TestViewExtendedAlpsValue(unittest.TestCase):
    """ViewExtendedAlpsValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ViewExtendedAlpsValue:
        """Test ViewExtendedAlpsValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ViewExtendedAlpsValue`
        """
        model = ViewExtendedAlpsValue()
        if include_optional:
            return ViewExtendedAlpsValue(
                commodity_id = 56,
                market_id = 56,
                price_type_id = 56,
                commodity_unit_id = 56,
                currency_id = 56,
                adm0_code = 56,
                country_name = '',
                commodity_price_date_year = 56,
                commodity_price_date_month = 56,
                commodity_price_date_week = 56,
                commodity_price_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                commodity_name = '',
                market_name = '',
                price_type_name = '',
                commodity_unit_name = '',
                currency_name = '',
                analysis_value_estimated_price = 1.337,
                analysis_value_pewi_value = 1.337,
                analysis_value_price_flag = ''
            )
        else:
            return ViewExtendedAlpsValue(
        )
        """

    def testViewExtendedAlpsValue(self):
        """Test ViewExtendedAlpsValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
