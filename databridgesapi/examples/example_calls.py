from api_connector import DataBridgesAPI
from datetime import date
import pandas as pd
from dotenv import load_dotenv
import numpy as np
import os

load_dotenv()  # take environment variables from .env.

api = DataBridgesAPI(api_key=os.environ['MY_KEY'], api_secret=os.environ['MY_SECRET'])
# Display available API
api_supported = api.show_supported_endpoint()
# Get Food Inflation for MLI
fi = api.get_economic_indicator(economic_indicator='food_inflation', iso3='MLI')
# Get Inflation rate for MLI
hi = api.get_economic_indicator(economic_indicator='headline_inflation', iso3='MLI')
# Get Inflation rate for MLI with starting date
hi_sd = api.get_economic_indicator(economic_indicator='headline_inflation', iso3='MLI', start_date=date(2023,1,1))
# Get Inflation rate for MLI with starting and ending date
hi_sd_ed = api.get_economic_indicator(economic_indicator='headline_inflation', iso3='MLI', start_date=date(2022,1,1), end_date=date(2022,3,1))
