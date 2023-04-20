"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501

    The version of the OpenAPI document: 1.3.1
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
from data_bridges_client.model.paged_commodity_list_dto import PagedCommodityListDTO


class CommoditiesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.commodities_categories_list_get_endpoint = _Endpoint(
            settings={
                'response_type': (PagedCommodityListDTO,),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/Commodities/Categories/List',
                'operation_id': 'commodities_categories_list_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'country_code',
                    'category_name',
                    'category_id',
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
                    'category_name':
                        (str,),
                    'category_id':
                        (int,),
                    'page':
                        (int,),
                    'format':
                        (str,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'country_code': 'countryCode',
                    'category_name': 'categoryName',
                    'category_id': 'categoryID',
                    'page': 'page',
                    'format': 'format',
                    'env': 'env',
                },
                'location_map': {
                    'country_code': 'query',
                    'category_name': 'query',
                    'category_id': 'query',
                    'page': 'query',
                    'format': 'query',
                    'env': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/json',
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.commodities_list_get_endpoint = _Endpoint(
            settings={
                'response_type': (PagedCommodityListDTO,),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/Commodities/List',
                'operation_id': 'commodities_list_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'country_code',
                    'commodity_name',
                    'commodity_id',
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
                    'commodity_name':
                        (str,),
                    'commodity_id':
                        (int,),
                    'page':
                        (int,),
                    'format':
                        (str,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'country_code': 'countryCode',
                    'commodity_name': 'commodityName',
                    'commodity_id': 'commodityID',
                    'page': 'page',
                    'format': 'format',
                    'env': 'env',
                },
                'location_map': {
                    'country_code': 'query',
                    'commodity_name': 'query',
                    'commodity_id': 'query',
                    'page': 'query',
                    'format': 'query',
                    'env': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/json',
                    'text/plain'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def commodities_categories_list_get(
        self,
        **kwargs
    ):
        """Provides the list of categories.  # noqa: E501

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  Categories are matched with high level WFP commodity classification at level 1. No mandatory parameter.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.commodities_categories_list_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            country_code (str): The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. [optional]
            category_name (str): The name, even partial and case insensitive, of a commodity category.. [optional]
            category_id (int): The exact ID of a Commodity, as found in /Commodities/List.. [optional] if omitted the server will use the default value of 0
            page (int): page number for paged results. [optional] if omitted the server will use the default value of 1
            format (str): Output format: [JSON|CSV] Json is the default value. [optional] if omitted the server will use the default value of "json"
            env (str): Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org. [optional]
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
            PagedCommodityListDTO
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
        return self.commodities_categories_list_get_endpoint.call_with_http_info(**kwargs)

    def commodities_list_get(
        self,
        **kwargs
    ):
        """Provide the detailed list of the commodities available in DataBridges platform  # noqa: E501

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  COICOP 2018 codes are returned to hierarchically matching categories based on [UN-Statistical Division codes](https://unstats.un.org/unsd/classifications/Econ/). No mandatory parameter.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.commodities_list_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            country_code (str): The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code. [optional]
            commodity_name (str): The name, even partial and case insensitive, of a commodity. [optional]
            commodity_id (int): The exact ID of a commodity. [optional] if omitted the server will use the default value of 0
            page (int): page number for paged results. [optional] if omitted the server will use the default value of 1
            format (str): Output format: [JSON|CSV] Json is the default value. [optional] if omitted the server will use the default value of "json"
            env (str): Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org. [optional]
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
            PagedCommodityListDTO
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
        return self.commodities_list_get_endpoint.call_with_http_info(**kwargs)

