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
from data_bridges_client.model.economic_indicator_property_paged_result import EconomicIndicatorPropertyPagedResult
from data_bridges_client.model.problem_details import ProblemDetails


class EconomicDataApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.economic_data_indicator_list_get_endpoint = _Endpoint(
            settings={
                'response_type': (EconomicIndicatorPropertyPagedResult,),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/EconomicData/IndicatorList',
                'operation_id': 'economic_data_indicator_list_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'indicator_name',
                    'iso3',
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
                    'page':
                        (int,),
                    'indicator_name':
                        (str,),
                    'iso3':
                        (str,),
                    'format':
                        (str,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'indicator_name': 'indicatorName',
                    'iso3': 'iso3',
                    'format': 'format',
                    'env': 'env',
                },
                'location_map': {
                    'page': 'query',
                    'indicator_name': 'query',
                    'iso3': 'query',
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
        self.economic_data_indicator_name_get_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'default'
                ],
                'endpoint_path': '/EconomicData/{indicatorName}',
                'operation_id': 'economic_data_indicator_name_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'indicator_name',
                    'page',
                    'iso3',
                    'start_date',
                    'end_date',
                    'format',
                    'env',
                ],
                'required': [
                    'indicator_name',
                ],
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
                    'indicator_name':
                        (str,),
                    'page':
                        (int,),
                    'iso3':
                        (str,),
                    'start_date':
                        (datetime,),
                    'end_date':
                        (datetime,),
                    'format':
                        (str,),
                    'env':
                        (str,),
                },
                'attribute_map': {
                    'indicator_name': 'indicatorName',
                    'page': 'page',
                    'iso3': 'iso3',
                    'start_date': 'startDate',
                    'end_date': 'endDate',
                    'format': 'format',
                    'env': 'env',
                },
                'location_map': {
                    'indicator_name': 'path',
                    'page': 'query',
                    'iso3': 'query',
                    'start_date': 'query',
                    'end_date': 'query',
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

    def economic_data_indicator_list_get(
        self,
        **kwargs
    ):
        """Returns the lists of indicators.  # noqa: E501

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  Returns the lists of indicators for which Vulnerability Analysis and Mapping - Economic and Market Analysis Unit has redistribution licensing from Trading Economics. No mandatory parameter.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.economic_data_indicator_list_get(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page number for paged results. [optional] if omitted the server will use the default value of 1
            indicator_name (str): Unique indicator name.. [optional] if omitted the server will use the default value of ""
            iso3 (str): The code to identify the country. Must be a ISO-3166 Alpha 3 code.. [optional] if omitted the server will use the default value of ""
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
            EconomicIndicatorPropertyPagedResult
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
        return self.economic_data_indicator_list_get_endpoint.call_with_http_info(**kwargs)

    def economic_data_indicator_name_get(
        self,
        indicator_name,
        **kwargs
    ):
        """Returns the time series of values for different indicators.  # noqa: E501

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access%20Policy-Open-green)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  Indicator name as retrieved from /EconomicData/IndicatorList is mandatory.    **Data Controller** - Wael Attia  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.economic_data_indicator_name_get(indicator_name, async_req=True)
        >>> result = thread.get()

        Args:
            indicator_name (str): Name of the indicator as found in /EconomicData/IndicatorList.

        Keyword Args:
            page (int): Page number for paged results. [optional] if omitted the server will use the default value of 1
            iso3 (str): The code to identify the country. Must be a ISO-3166 Alpha 3 code.. [optional] if omitted the server will use the default value of ""
            start_date (datetime): Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24). [optional]
            end_date (datetime): Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24). [optional]
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
        kwargs['indicator_name'] = \
            indicator_name
        return self.economic_data_indicator_name_get_endpoint.call_with_http_info(**kwargs)

