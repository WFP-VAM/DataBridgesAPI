# import data_bridges_client
# from data_bridges_client.rest import ApiException
# from data_bridges_client.token import WfpApiToken

def test_import():
    print("hello world")

class DataBridges:
    def __init__(self, api_key, api_secret, env='prod'):
        self.access_token = WfpApiToken(api_key, api_secret)

        self.config = data_bridges_client.Configuration(
            host=f"https://api.wfp.org/vam-data-bridges/2.0.0",
            access_token=self.access_token
        )
        self.client = data_bridges_client.ApiClient(self.config)
        self.commodities_api = CommoditiesApi(self.client)
        self.env = env

    def get_commodity_categories(self, country_code=None, category_name=None, category_id=0, page=1, format='json'):
        """
        Get a list of commodity categories.

        Args:
            country_code (str, optional): The code to identify the country.
            category_name (str, optional): The name, even partial and case insensitive, of a commodity category.
            category_id (int, optional): The exact ID of a Commodity. Defaults to 0.
            page (int, optional): Page number for paged results. Defaults to 1.
            format (str, optional): Output format: [JSON|CSV]. Defaults to 'json'.

        Returns:
            The API response containing the list of commodity categories.
        """
        try:
            response = self.commodities_api.commodities_categories_list_get(
                country_code=country_code,
                category_name=category_name,
                category_id=category_id,
                page=page,
                format=format,
                env=self.env
            )
            return response
        except Exception as e:
            print(f"Error: {e}")
