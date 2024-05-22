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

from data_bridges_client.models.economic_indicator_property_paged_result import EconomicIndicatorPropertyPagedResult

class TestEconomicIndicatorPropertyPagedResult(unittest.TestCase):
    """EconomicIndicatorPropertyPagedResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EconomicIndicatorPropertyPagedResult:
        """Test EconomicIndicatorPropertyPagedResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EconomicIndicatorPropertyPagedResult`
        """
        model = EconomicIndicatorPropertyPagedResult()
        if include_optional:
            return EconomicIndicatorPropertyPagedResult(
                items = [
                    {
                        'key' : null
                        }
                    ],
                page = 56,
                total_items = 56
            )
        else:
            return EconomicIndicatorPropertyPagedResult(
        )
        """

    def testEconomicIndicatorPropertyPagedResult(self):
        """Test EconomicIndicatorPropertyPagedResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
