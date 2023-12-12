import time
import ast
import argparse
from dotenv import load_dotenv

import data_bridges_client
from pprint import pprint
from data_bridges_client.api import food_security_api, gorp_api
from data_bridges_client.model.bad_request_dto import BadRequestDTO
import os
from data_bridges_client.token import WfpApiToken
import pandas as pd

# Configure OAuth2 access token for authorization: default
base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '.env'))
KEY = os.getenv("KEY")
SECRET = os.getenv("SECRET")
token = WfpApiToken(api_key=KEY, api_secret=SECRET)

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Query an API endpoint and get the response.')
parser.add_argument('endpoint', type=str, help='The API endpoint to query.')
args = parser.parse_args()

# Enter a context with an instance of the API client using a fresh token
with data_bridges_client.ApiClient(token.refresh_configuration()) as api_client:
    # Create an instance of the API class

    env = "prod" # str | Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org (optional)

    try:
    # Call the specified API endpoint
        if args.endpoint.lower() == 'ipc':
            api_instance = food_security_api.FoodSecurityApi(api_client)
            response = api_instance.food_security_list_get(env=env)
        elif args.endpoint.lower() == 'gorp':
            api_instance = gorp_api.GorpApi(api_client)
            response = api_instance.gorp_latest_get(env=env)
        # Add more elif statements for other endpoints as needed

        # Convert the 'items' list in the response to a DataFrame
        # Convert the 'items' list in the response to a DataFrame
        df = pd.DataFrame(response['items'])

        # Write the DataFrame to a CSV file
        df.to_csv(f'{args.endpoint.lower()}_output.csv', index=False)
        print("Downloaded data to %s_output.csv" % args.endpoint.lower())
        print("Downloaded data to %s_output.csv" % args.endpoint.lower())
    except data_bridges_client.ApiException as e:
        print("Exception when calling CommoditiesApi->commodities_list_get: %s\n" % e)