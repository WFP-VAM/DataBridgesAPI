"""
Read a 'full' Household dataset  from Data Bridges and load it into STATA.
Only works if user has STATA 18+ installed and added to PATH.
"""

from data_bridges_utils.get_data import shapes_get_survey
from data_bridges_utils.load_stata import test_load_stata

config_path = r"data_bridges_api_config.yaml"

survey_data = shapes_get_survey(surveyid=3329, yamlpath=config_path, access_type='full')
price_data = shapes_get_prices(country_iso3='AFG', yamlpath=config_path, survey_date='2024-12-01')
exchange_rates_data = shapes_get_exchangerates(country_iso3='AFG', yamlpath=config_path)


ds = load_stata(survey_data)