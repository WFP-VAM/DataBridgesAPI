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

from data_bridges_client.api.surveys_api import SurveysApi


class TestSurveysApi(unittest.TestCase):
    """SurveysApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SurveysApi()

    def tearDown(self) -> None:
        pass

    def test_m_fi_surveys_base_data_get(self) -> None:
        """Test case for m_fi_surveys_base_data_get

        Get data that includes the core Market Functionality Index (MFI) fields only by Survey ID
        """
        pass

    def test_m_fi_surveys_full_data_get(self) -> None:
        """Test case for m_fi_surveys_full_data_get

        Get a full dataset that includes all the fields included in the survey in addition to the core Market Functionality Index (MFI) fields by Survey ID. To access this data, please contact global.mfi@wfp.org for authorization.
        """
        pass

    def test_m_fi_surveys_get(self) -> None:
        """Test case for m_fi_surveys_get

        Retrieve 1) Survey IDs, 2) their corresponding XLS Form IDs, and 3) Base XLS Form of all MFI surveys conducted in a country.   A date of reference, SurveyDate, for the data collection is set by the officer responsible for the upload for each survey.
        """
        pass

    def test_m_fi_surveys_processed_data_get(self) -> None:
        """Test case for m_fi_surveys_processed_data_get

        Get a MFI processed data in long format; levels indicate the data aggregation level 1) Normalized Score, 2) Trader Aggregate Score,   3) Market Aggregate Score, 4) Trader Median, 5) Trader Mean, 6) Market Mean; each line corresponds to one of the nine dimensions of scores   plus the final MFI aggregate score; 1) Assortment, 2) Availability, 3) Price, 4) Resilience, 5) Competition, 6) Infrastructure, 7) Service,   8) Quality, 9) Access and Protection, and 10) MFI final score; the variable label describes each variable and its value range
        """
        pass


if __name__ == '__main__':
    unittest.main()
