import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from data_bridges_client import ApiClient, IncubationApi, ApiException
from data_bridges_utils.get_data import GetData

class TestGetHouseholdSurvey(unittest.TestCase):

    def setUp(self):
        self.get_data = GetData()
        self.survey_id = "test_survey_id"
        self.access_type = "public"
        self.page_size = 200

    @patch('data_bridges_utils.get_data.ApiClient')
    @patch('data_bridges_utils.get_data.IncubationApi')
    def test_get_household_survey_success(self, mock_incubation_api, mock_api_client):
        mock_api_instance = mock_incubation_api.return_value
        mock_api_instance.household_public_base_data_get.return_value = MagicMock(
            items=[{'key': 'value'}],
            total_items=1
        )

        result = self.get_data.get_household_survey(self.survey_id, self.access_type, self.page_size)

        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(len(result), 1)

    @patch('data_bridges_utils.get_data.ApiClient')
    @patch('data_bridges_utils.get_data.IncubationApi')
    def test_get_household_survey_api_exception(self, mock_incubation_api, mock_api_client):
        mock_api_instance = mock_incubation_api.return_value
        mock_api_instance.household_public_base_data_get.side_effect = ApiException("API Exception")

        with self.assertRaises(SystemExit):
            self.get_data.get_household_survey(self.survey_id, self.access_type, self.page_size)

    def test_get_household_survey_invalid_access_type(self):
        invalid_access_type = "invalid_type"
        with self.assertRaises(KeyError):
            self.get_data.get_household_survey(self.survey_id, invalid_access_type, self.page_size)

if __name__ == '__main__':
    unittest.main()
