"""
Read a 'full' Household dataset  from Data Bridges and load it into STATA.
Only works if user has STATA 18+ installed and added to PATH.
"""

from data_bridges_utils import DataBridgesShapes, load_stata

CONFIG_PATH = r"data_bridges_api_config.yaml"

# Initialize DataBridges client with credentials from YAML file
client = DataBridgesShapes(CONFIG_PATH)

# Get houhold data for survey id
survey_data = client.get_household_survey(survey_id=3329, access_type='full')

# Load into STATA dataframe
ds = load_stata(survey_data)