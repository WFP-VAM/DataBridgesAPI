#%% FROM PYTHON
from data_bridges_utils.get_data import shapes_get_survey, shapes_get_prices, shapes_get_exchangerates

config_path = r"path\data_bridges_api_config.yaml"


survey_data = shapes_get_survey(surveyid=3329, yamlpath=config_path, access_type='full')
# price_data = shapes_get_prices(country_iso3='AFG', yamlpath=yaml_file_path, survey_date='2024-12-01')
# exchange_rates_data = shapes_get_exchangerates(country_iso3='AFG', yamlpath=yaml_file_path)

print(survey_data.head())

#%%
# # FOR STATA USERS
# from data_bridges_utils.get_data import shapes_get_survey
# from data_bridges_utils.load_stata import load_stata

# df = shapes_get_survey(surveyid=3329, yamlpath=yaml_file_path, access_type='full'), 'Newframe')
# ds = load_stata(df)

# %%
