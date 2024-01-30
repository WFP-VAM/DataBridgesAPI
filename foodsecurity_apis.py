import os
from dotenv import load_dotenv
import data_bridges_client
from data_bridges_client.api import food_security_api, gorp_api
from data_bridges_client.token import WfpApiToken
import pandas as pd


def get_api_client():
    """
    Returns an API client for accessing the Data Bridges API.

    This function retrieves the API key and secret from the environment variables,
    creates an API token using the key and secret, and initializes an API client
    with the token's refresh configuration.

    Returns:
        data_bridges_client.ApiClient: An API client for accessing the Data Bridges API.
    """
    base_dir = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(base_dir, '.env'))
    consumer_key = os.getenv("KEY")
    consumer_secret = os.getenv("SECRET")
    token = WfpApiToken(api_key=kconsumer_keyey, api_secret=consumer_secret)
    return data_bridges_client.ApiClient(token.refresh_configuration())


def get_endpoint_data(api_client, endpoint):
    """
    Retrieves data from the specified endpoint using the provided API client.

    Args:
        api_client (object): The API client object used to make API requests.
        endpoint (str): The endpoint to retrieve data from. Valid values are 'ipc' or 'gorp'.

    Returns:
        list: The list of items retrieved from the specified endpoint.

    Raises:
        ValueError: If an invalid endpoint is provided.
    """
    env = "prod"
    if endpoint.lower() == 'ipc':
        api_instance = food_security_api.FoodSecurityApi(api_client)
        response = api_instance.food_security_list_get(env=env)
    elif endpoint.lower() == 'gorp':
        api_instance = gorp_api.GorpApi(api_client)
        response = api_instance.gorp_latest_get(env=env)
    else:
        raise ValueError("Invalid endpoint. Please enter either 'ipc' or 'gorp'.")
    return response['items']


def save_data_to_csv(data, filename):
    """
    Save data to a CSV file.

    Args:
        data (list): A list of objects containing data to be saved.
        filename (str): The name of the CSV file to be created.

    Returns:
        None
    """
    dicts = [item._data_store for item in data]
    df = pd.DataFrame(dicts)
    df.to_csv(filename, index=False)
    print(f"Downloaded data to {filename}")

def main():
    """
    This function is the entry point of the script.
    It prompts the user to enter an endpoint (ipc or gorp),
    retrieves the data from the API using the specified endpoint,
    and saves the data to a CSV file.
    """
    api_client = get_api_client()
    endpoint = input("Please enter the endpoint (ipc or gorp): ").lower()
    try:
        data = get_endpoint_data(api_client, endpoint)
        save_data_to_csv(data, f'{endpoint}_output.csv')
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()