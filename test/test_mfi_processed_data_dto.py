# coding: utf-8

"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

    The version of the OpenAPI document: 5.0.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from data_bridges_client.models.mfi_processed_data_dto import MFIProcessedDataDTO

class TestMFIProcessedDataDTO(unittest.TestCase):
    """MFIProcessedDataDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MFIProcessedDataDTO:
        """Test MFIProcessedDataDTO
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MFIProcessedDataDTO`
        """
        model = MFIProcessedDataDTO()
        if include_optional:
            return MFIProcessedDataDTO(
                survey_id = 56,
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                market_id = 56,
                market_name = '',
                market_latitude = 1.337,
                market_longitude = 1.337,
                regional_bureau_id = 56,
                regional_bureau_name = '',
                adm0_code = 56,
                adm0_name = '',
                adm1_code = 56,
                adm1_name = '',
                adm2_code = 56,
                adm2_name = '',
                level_id = 56,
                level_name = '',
                dimension_id = 56,
                dimension_name = '',
                variable_id = 56,
                variable_name = '',
                variable_label = '',
                output_value = 1.337,
                traders_sample_size = 56,
                base_xls_form_id = 56,
                base_xls_form_name = ''
            )
        else:
            return MFIProcessedDataDTO(
        )
        """

    def testMFIProcessedDataDTO(self):
        """Test MFIProcessedDataDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
