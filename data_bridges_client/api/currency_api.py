"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501

    The version of the OpenAPI document: 4.0.0
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
from data_bridges_client.model.paged_currency_list_dto import PagedCurrencyListDTO
from data_bridges_client.model.usd_indirect_quotation_paged_result import UsdIndirectQuotationPagedResult


class CurrencyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.currency_list_get_endpoint = _Endpoint(
            settings={
                'response_type': (PagedCurrencyListDTO,),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/Currency/List',
                'operation_id': 'currency_list_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'country_code',
                    'currency_name',
                    'currency_id',
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
                    'currency_name':
                        (str,),
                    'currency_id':
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
                    'currency_name': 'currencyName',
                    'currency_id': 'currencyID',
                    'page': 'page',
                    'format': 'format',
                    'env': 'env',
                },
                'location_map': {
                    'country_code': 'query',
                    'currency_name': 'query',
                    'currency_id': 'query',
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
        self.currency_usd_indirect_quotation_get_endpoint = _Endpoint(
            settings={
                'response_type': (UsdIndirectQuotationPagedResult,),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/Currency/UsdIndirectQuotation',
                'operation_id': 'currency_usd_indirect_quotation_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'country_iso3',
                    'currency_name',
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
                    'country_iso3':
                        (str,),
                    'currency_name':
                        (str,),
                    'page':
                        (int,),
                    'format':
                        (str,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'country_iso3': 'countryIso3',
                    'currency_name': 'currencyName',
                    'page': 'page',
                    'format': 'format',
                    'env': 'env',
                },
                'location_map': {
                    'country_iso3': 'query',
                    'currency_name': 'query',
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

    def currency_list_get(
        self,
        **kwargs
    ):
        """Returns the list of currencies available in the internal VAM database, with Currency 3-letter code, matching with ISO 4217.  # noqa: E501

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_currency-list_get\"      **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.currency_list_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            country_code (str): The code to identify the country. It can be a ISO-3166 Alpha 3 code or the VAM internal admin0code.. [optional]
            currency_name (str): Currency 3-letter code, matching with ISO 4217.. [optional]
            currency_id (int): Unique code to identify the currency in internal VAM currencies.. [optional] if omitted the server will use the default value of 0
            page (int): Page number for paged results. [optional] if omitted the server will use the default value of 1
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
            PagedCurrencyListDTO
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
        return self.currency_list_get_endpoint.call_with_http_info(**kwargs)

    def currency_usd_indirect_quotation_get(
        self,
        **kwargs
    ):
        """Returns the value of the Exchange rates from Trading Economics, for official rates, and DataViz for unofficial rates.  # noqa: E501

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-Approval_Required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_currency-usdindirectquotation_get\"  Returns the time series of values of the Exchange rate of the Local Currency for buying 1 USD in the official market. Original frequency for official rates is daily, non-indicated. Unofficial rates are aggregated at national level by the original frequency of collection. For greater detail on unofficial exchange rates, explore the Exchange Rate (unofficial) commodity in Market Prices Prices. No mandatory parameter.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.currency_usd_indirect_quotation_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            country_iso3 (str): The code to identify the country. Must be a ISO-3166 Alpha 3 code.. [optional] if omitted the server will use the default value of ""
            currency_name (str): the ISO3 code for the currency, based on ISO4217. [optional] if omitted the server will use the default value of ""
            page (int): Page number for paged results. [optional] if omitted the server will use the default value of 1
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
            UsdIndirectQuotationPagedResult
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
        return self.currency_usd_indirect_quotation_get_endpoint.call_with_http_info(**kwargs)

