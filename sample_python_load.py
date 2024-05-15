
"""
Read Household Data from Data Bridges and load it into STATA.
Only works if user has STATA 18+ installed and added to PATH.
"""
from data_bridges_utils.get_data import DataBridgesShapes

CONFIG_PATH = r"data_bridges_api_config.yaml"

client = DataBridgesShapes(CONFIG_PATH)


# survey_data = client.get_household_survey(3329, 'full')
# print(survey_data.head())

# price_data = client.get_prices("country_iso3", "survey_date")
# exchange_rates = client.get_exchangerates("country_iso3")

food_sec = client.get_ipc_equivalent("AFG", 2023)

print(food_sec.head())



# %%
