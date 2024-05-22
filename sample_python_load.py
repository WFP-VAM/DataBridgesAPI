
"""
Read Household Data from Data Bridges and load it into STATA.
Only works if user has STATA 18+ installed and added to PATH.
"""
from data_bridges_utils import DataBridgesShapes

CONFIG_PATH = r"data_bridges_api_config.yaml"

client = DataBridgesShapes(CONFIG_PATH)

# Get houhold data for survey id
survey_data = client.get_household_survey(survey_id=3329, access_type='full')
print(survey_data.head())

# TODO: other API calls, including GORP and IPC
# food_sec = client.get_ipc_equivalent("AFG", 2023)
# print(food_sec.head())
