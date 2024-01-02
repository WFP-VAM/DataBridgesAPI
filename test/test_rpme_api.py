"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import data_bridges_client
from data_bridges_client.api.rpme_api import RpmeApi  # noqa: E501


class TestRpmeApi(unittest.TestCase):
    """RpmeApi unit test stubs"""

    def setUp(self):
        self.api = RpmeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_rpme_base_data_get(self):
        """Test case for rpme_base_data_get

        Get data that includes the core RPME fields only by Survey ID  # noqa: E501
        """
        pass

    def test_rpme_full_data_get(self):
        """Test case for rpme_full_data_get

        Get a full dataset that includes all the fields included in the survey in addition to the core RPME fields by Survey ID.  # noqa: E501
        """
        pass

    def test_rpme_output_values_get(self):
        """Test case for rpme_output_values_get

        Processed values for each variable used in the assessments  # noqa: E501
        """
        pass

    def test_rpme_surveys_get(self):
        """Test case for rpme_surveys_get

        Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all RPME surveys conducted in a country. The date of reference, SurveyDate, for the data collection is set by the officer responsible for the upload of each survey.  # noqa: E501
        """
        pass

    def test_rpme_variables_get(self):
        """Test case for rpme_variables_get

        List of variables  # noqa: E501
        """
        pass

    def test_rpme_xls_forms_get(self):
        """Test case for rpme_xls_forms_get

        Get a complete list of XLS Forms uploaded on the RPME in a given period of data collection. This is the digital version of the questionnaire used during the data collection exercise.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
