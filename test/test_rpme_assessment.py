# coding: utf-8

"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

    The version of the OpenAPI document: 4.0.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from data_bridges_client.models.rpme_assessment import RpmeAssessment

class TestRpmeAssessment(unittest.TestCase):
    """RpmeAssessment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RpmeAssessment:
        """Test RpmeAssessment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RpmeAssessment`
        """
        model = RpmeAssessment()
        if include_optional:
            return RpmeAssessment(
                survey_id = 56,
                assessment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                shop_id = 56,
                adm0_code = 56,
                adm1_code = 56,
                adm2_code = 56,
                adm0_code_dots = '',
                adm1_code_dots = '',
                adm2_code_dots = '',
                market_id = 56,
                sh_latitude = 1.337,
                sh_longitude = 1.337,
                nb_beneficiaries_interviewed = 56,
                price_score_tbu = True,
                price_score_tbd = True,
                beneficiaries_score_tbu = True,
                trd_name = '',
                sev_cntr_dev = '',
                ben_sev_cntr_dev = '',
                output_values = [
                    {
                        'key' : null
                        }
                    ]
            )
        else:
            return RpmeAssessment(
        )
        """

    def testRpmeAssessment(self):
        """Test RpmeAssessment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
