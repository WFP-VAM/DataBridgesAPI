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

from data_bridges_client.models.household_survey_list_dto import HouseholdSurveyListDTO

class TestHouseholdSurveyListDTO(unittest.TestCase):
    """HouseholdSurveyListDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HouseholdSurveyListDTO:
        """Test HouseholdSurveyListDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HouseholdSurveyListDTO`
        """
        model = HouseholdSurveyListDTO()
        if include_optional:
            return HouseholdSurveyListDTO(
                survey_id = 56,
                survey_status_id = 56,
                survey_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                survey_end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                survey_create_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                survey_validation_report = '',
                survey_original_filename = '',
                xls_form_name = '',
                base_xls_form_name = '',
                country_name = '',
                adm0_code = 56,
                iso3_alpha3 = '',
                user_name = '',
                approved_by = '',
                original_csv_file = '',
                base_data = '',
                survey_attributes = [
                    {
                        'key' : null
                        }
                    ],
                organizations = [
                    {
                        'key' : null
                        }
                    ],
                survey_modality_name = '',
                survey_category_name = '',
                survey_sub_category_name = '',
                survey_phase_name = '',
                survey_visibilty = '',
                is_continuous_monitoring = True,
                survey_name = ''
            )
        else:
            return HouseholdSurveyListDTO(
        )
        """

    def testHouseholdSurveyListDTO(self):
        """Test HouseholdSurveyListDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
