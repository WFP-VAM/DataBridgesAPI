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

from data_bridges_client.models.ipc_value import IpcValue

class TestIpcValue(unittest.TestCase):
    """IpcValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IpcValue:
        """Test IpcValue
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IpcValue`
        """
        model = IpcValue()
        if include_optional:
            return IpcValue(
                ipc_id = 56,
                ipc_year = 56,
                ipc_update_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                iso3_alpha3 = '',
                ipc_country_name = '',
                ipc_area_name = '',
                ipc_phase3_population = 56,
                ipc_phase4_population = 56,
                ipc_phase5_population = 56,
                ipc_phase35population = 56,
                ipc_phase45population = 56,
                ipc_phase3_percentage = 1.337,
                ipc_phase4_percentage = 1.337,
                ipc_phase5_percentage = 1.337,
                ipc_phase35percentage = 1.337,
                ipc_phase45percentage = 1.337,
                ipc_analysed_population = 56,
                ipc_analysed_percentage = 1.337,
                ipc_analysis_comment = '',
                ipc_data_type = '',
                ipc_data_source = '',
                ipc_reference_period = '',
                ipc_create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                ipc_show_on_data_viz = True,
                ipc_is_latest_value = True
            )
        else:
            return IpcValue(
        )
        """

    def testIpcValue(self):
        """Test IpcValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
