from api_connector import DataBridgesAPI
from datetime import date
import dateutil.relativedelta
import pandas as pd
from dotenv import load_dotenv
import numpy as np
import os

load_dotenv()  # take environment variables from .env.

api = DataBridgesAPI(api_key=os.environ['MY_KEY'], api_secret=os.environ['MY_SECRET'])

today = date.today()
delta = dateutil.relativedelta.relativedelta(months=6)
six_months_ago = today - delta

# Get Alps DATA
alpsData = api.get_monthly_alps('GNB', six_months_ago)

# Get Commodity list for GNB
commodities = api.get_commodity_list('GNB')
commodities = pd.json_normalize(commodities)

# =======================
# Work on ALPS Data
# =======================
alpsData = pd.json_normalize(alpsData)
# Get only food commodities
foodCommodities = commodities.loc[commodities.categoryId < 8,['categoryId', 'id', 'name']]
subsetAlpsData = alpsData.set_index('commodityID').join(foodCommodities.set_index('id'), how='inner')
priceData = pd.df(alpsData)

conditions = [
    subsetAlpsData['categoryId'] == 1,
    subsetAlpsData['categoryId'] == 2,
    subsetAlpsData['categoryId'] == 3,
    subsetAlpsData['categoryId'] == 4,
    subsetAlpsData['categoryId'] == 5,
    subsetAlpsData['categoryId'] == 6,
    subsetAlpsData['categoryId'] == 7,
]

outputs = [
    2, 4, 4, 1, 3, 0.5, 0.5
]

res = pd.DataFrame(np.select(conditions, outputs, 0))
