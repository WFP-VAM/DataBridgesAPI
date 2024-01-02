"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import data_bridges_client
from data_bridges_client.api.xls_forms_api import XlsFormsApi  # noqa: E501


class TestXlsFormsApi(unittest.TestCase):
    """XlsFormsApi unit test stubs"""

    def setUp(self):
        self.api = XlsFormsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_m_fi_xls_forms_definition_get(self):
        """Test case for m_fi_xls_forms_definition_get

        Get a complete set of XLS Form definitions of a given XLS Form ID. This is the digital version of the questionnaire used during the data collection exercise.  # noqa: E501
        """
        pass

    def test_m_fi_xls_forms_get(self):
        """Test case for m_fi_xls_forms_get

        Get a complete list of XLS Forms uploaded on the MFI Data Bridge in a given period of data collection. This is the digital version of the questionnaire used during the data collection exercise.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
