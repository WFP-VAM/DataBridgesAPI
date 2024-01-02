"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from data_bridges_client.api_client import ApiClient, Endpoint as _Endpoint
from data_bridges_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from data_bridges_client.model.bad_request_dto import BadRequestDTO
from data_bridges_client.model.i_feature import IFeature
from data_bridges_client.model.nearby_markets_dto import NearbyMarketsDTO


class MarketsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.markets_geo_json_list_get_endpoint = _Endpoint(
            settings={
                'response_type': ([IFeature],),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/Markets/GeoJSONList',
                'operation_id': 'markets_geo_json_list_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'adm0code',
                    'env',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'env',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('env',): {

                        "PROD": "prod",
                        "DEV": "dev"
                    },
                },
                'openapi_types': {
                    'adm0code':
                        (int,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'adm0code': 'adm0code',
                    'env': 'env',
                },
                'location_map': {
                    'adm0code': 'query',
                    'env': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/geo+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.markets_list_get_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/Markets/List',
                'operation_id': 'markets_list_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'country_code',
                    'page',
                    'format',
                    'env',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'env',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('env',): {

                        "PROD": "prod",
                        "DEV": "dev"
                    },
                },
                'openapi_types': {
                    'country_code':
                        (str,),
                    'page':
                        (int,),
                    'format':
                        (str,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'country_code': 'countryCode',
                    'page': 'page',
                    'format': 'format',
                    'env': 'env',
                },
                'location_map': {
                    'country_code': 'query',
                    'page': 'query',
                    'format': 'query',
                    'env': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.markets_markets_as_csv_get_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/Markets/MarketsAsCSV',
                'operation_id': 'markets_markets_as_csv_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'adm0code',
                    'local_names',
                    'env',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'env',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('env',): {

                        "PROD": "prod",
                        "DEV": "dev"
                    },
                },
                'openapi_types': {
                    'adm0code':
                        (int,),
                    'local_names':
                        (bool,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'adm0code': 'adm0code',
                    'local_names': 'localNames',
                    'env': 'env',
                },
                'location_map': {
                    'adm0code': 'query',
                    'local_names': 'query',
                    'env': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/plain',
                    'application/json',
                    'text/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.markets_nearby_markets_get_endpoint = _Endpoint(
            settings={
                'response_type': ([NearbyMarketsDTO],),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/Markets/NearbyMarkets',
                'operation_id': 'markets_nearby_markets_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'adm0code',
                    'lat',
                    'lng',
                    'env',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'env',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('env',): {

                        "PROD": "prod",
                        "DEV": "dev"
                    },
                },
                'openapi_types': {
                    'adm0code':
                        (int,),
                    'lat':
                        (float,),
                    'lng':
                        (float,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'adm0code': 'adm0code',
                    'lat': 'lat',
                    'lng': 'lng',
                    'env': 'env',
                },
                'location_map': {
                    'adm0code': 'query',
                    'lat': 'query',
                    'lng': 'query',
                    'env': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def markets_geo_json_list_get(
        self,
        **kwargs
    ):
        """Provide a list of geo referenced markets in a specific country  # noqa: E501

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.markets_geo_json_list_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            adm0code (int): The admin code of the country. [optional]
            env (str): Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [IFeature]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.markets_geo_json_list_get_endpoint.call_with_http_info(**kwargs)

    def markets_list_get(
        self,
        **kwargs
    ):
        """Get a complete list of markets in a country  # noqa: E501

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.markets_list_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            country_code (str): The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. [optional]
            page (int): page number for paged results. [optional] if omitted the server will use the default value of 1
            format (str): Output format: [JSON|CSV] Json is the default value. [optional] if omitted the server will use the default value of "json"
            env (str): Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            file_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.markets_list_get_endpoint.call_with_http_info(**kwargs)

    def markets_markets_as_csv_get(
        self,
        **kwargs
    ):
        """Get a complete list of markets in a country  # noqa: E501

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.markets_markets_as_csv_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            adm0code (int): The admin code of the country. [optional]
            local_names (bool): If true the name of markets and regions will be localized if available. [optional] if omitted the server will use the default value of False
            env (str): Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            file_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.markets_markets_as_csv_get_endpoint.call_with_http_info(**kwargs)

    def markets_nearby_markets_get(
        self,
        **kwargs
    ):
        """Find markets near a given location by longitude and latitude within a 15Km distance  # noqa: E501

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.markets_nearby_markets_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            adm0code (int): code for the country as retrieved from https://api.vam.wfp.org/geodata/CountriesInRegion. [optional]
            lat (float): latitude of the point that will be used to search for existing nearby markets. Geo-reference standard used for this coordinate is decimal. [optional]
            lng (float): longitude of the point that will be used to search for existing nearby markets.  Geo-reference standard used for this coordinate is decimal. [optional]
            env (str): Environment.   * `prod` - api.vam.wfp.org   * `dev` - api.vam.wfp.org. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [NearbyMarketsDTO]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.markets_nearby_markets_get_endpoint.call_with_http_info(**kwargs)

