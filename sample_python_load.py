
"""
Read Household Data from Data Bridges and load it into STATA.
Only works if user has STATA 18+ installed and added to PATH.
"""
from data_bridges_utils.get_data import shapes_get_survey

config_path = r"data_bridges_api_config.yaml"


survey_data = shapes_get_survey(surveyid=3329, yamlpath=config_path, access_type='full')
price_data = shapes_get_prices(country_iso3='AFG', yamlpath=config_path, survey_date='2024-12-01')
exchange_rates_data = shapes_get_exchangerates(country_iso3='AFG', yamlpath=config_path)

print(survey_data.head())



# %%