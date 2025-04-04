# coding: utf-8

"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

    The version of the OpenAPI document: 6.0.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from datetime import datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from data_bridges_client.models.economic_indicator_property_paged_result import EconomicIndicatorPropertyPagedResult
from data_bridges_client.models.paged_economic_data_dto import PagedEconomicDataDTO

from data_bridges_client.api_client import ApiClient, RequestSerialized
from data_bridges_client.api_response import ApiResponse
from data_bridges_client.rest import RESTResponseType


class EconomicDataApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def economic_data_indicator_list_get(
        self,
        page: Annotated[Optional[StrictInt], Field(description="Page number for paged results")] = None,
        indicator_name: Annotated[Optional[StrictStr], Field(description="Unique indicator name.")] = None,
        iso3: Annotated[Optional[StrictStr], Field(description="The code to identify the country. Must be a ISO-3166 Alpha 3 code.")] = None,
        format: Annotated[Optional[StrictStr], Field(description="Output format: [JSON|CSV] Json is the default value")] = None,
        env: Annotated[Optional[StrictStr], Field(description="Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> EconomicIndicatorPropertyPagedResult:
        """Returns the lists of indicators.

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_economicdata-indicatorlist_get\"  Returns the lists of indicators for which Vulnerability Analysis and Mapping - Economic and Market Analysis Unit has redistribution licensing from Trading Economics. No mandatory parameter.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

        :param page: Page number for paged results
        :type page: int
        :param indicator_name: Unique indicator name.
        :type indicator_name: str
        :param iso3: The code to identify the country. Must be a ISO-3166 Alpha 3 code.
        :type iso3: str
        :param format: Output format: [JSON|CSV] Json is the default value
        :type format: str
        :param env: Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org
        :type env: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._economic_data_indicator_list_get_serialize(
            page=page,
            indicator_name=indicator_name,
            iso3=iso3,
            format=format,
            env=env,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EconomicIndicatorPropertyPagedResult",
            '400': "BadRequestDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def economic_data_indicator_list_get_with_http_info(
        self,
        page: Annotated[Optional[StrictInt], Field(description="Page number for paged results")] = None,
        indicator_name: Annotated[Optional[StrictStr], Field(description="Unique indicator name.")] = None,
        iso3: Annotated[Optional[StrictStr], Field(description="The code to identify the country. Must be a ISO-3166 Alpha 3 code.")] = None,
        format: Annotated[Optional[StrictStr], Field(description="Output format: [JSON|CSV] Json is the default value")] = None,
        env: Annotated[Optional[StrictStr], Field(description="Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[EconomicIndicatorPropertyPagedResult]:
        """Returns the lists of indicators.

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_economicdata-indicatorlist_get\"  Returns the lists of indicators for which Vulnerability Analysis and Mapping - Economic and Market Analysis Unit has redistribution licensing from Trading Economics. No mandatory parameter.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

        :param page: Page number for paged results
        :type page: int
        :param indicator_name: Unique indicator name.
        :type indicator_name: str
        :param iso3: The code to identify the country. Must be a ISO-3166 Alpha 3 code.
        :type iso3: str
        :param format: Output format: [JSON|CSV] Json is the default value
        :type format: str
        :param env: Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org
        :type env: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._economic_data_indicator_list_get_serialize(
            page=page,
            indicator_name=indicator_name,
            iso3=iso3,
            format=format,
            env=env,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EconomicIndicatorPropertyPagedResult",
            '400': "BadRequestDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def economic_data_indicator_list_get_without_preload_content(
        self,
        page: Annotated[Optional[StrictInt], Field(description="Page number for paged results")] = None,
        indicator_name: Annotated[Optional[StrictStr], Field(description="Unique indicator name.")] = None,
        iso3: Annotated[Optional[StrictStr], Field(description="The code to identify the country. Must be a ISO-3166 Alpha 3 code.")] = None,
        format: Annotated[Optional[StrictStr], Field(description="Output format: [JSON|CSV] Json is the default value")] = None,
        env: Annotated[Optional[StrictStr], Field(description="Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Returns the lists of indicators.

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_economicdata-indicatorlist_get\"  Returns the lists of indicators for which Vulnerability Analysis and Mapping - Economic and Market Analysis Unit has redistribution licensing from Trading Economics. No mandatory parameter.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

        :param page: Page number for paged results
        :type page: int
        :param indicator_name: Unique indicator name.
        :type indicator_name: str
        :param iso3: The code to identify the country. Must be a ISO-3166 Alpha 3 code.
        :type iso3: str
        :param format: Output format: [JSON|CSV] Json is the default value
        :type format: str
        :param env: Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org
        :type env: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._economic_data_indicator_list_get_serialize(
            page=page,
            indicator_name=indicator_name,
            iso3=iso3,
            format=format,
            env=env,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "EconomicIndicatorPropertyPagedResult",
            '400': "BadRequestDTO",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _economic_data_indicator_list_get_serialize(
        self,
        page,
        indicator_name,
        iso3,
        format,
        env,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if page is not None:
            
            _query_params.append(('page', page))
            
        if indicator_name is not None:
            
            _query_params.append(('indicatorName', indicator_name))
            
        if iso3 is not None:
            
            _query_params.append(('iso3', iso3))
            
        if format is not None:
            
            _query_params.append(('format', format))
            
        if env is not None:
            
            _query_params.append(('env', env))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'text/plain', 
                    'application/json', 
                    'text/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'default'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/EconomicData/IndicatorList',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def economic_data_indicator_name_get(
        self,
        indicator_name: Annotated[StrictStr, Field(description="Name of the indicator as found in /EconomicData/IndicatorList.")],
        page: Annotated[Optional[StrictInt], Field(description="Page number for paged results")] = None,
        iso3: Annotated[Optional[StrictStr], Field(description="The code to identify the country. Must be a ISO-3166 Alpha 3 code.")] = None,
        start_date: Annotated[Optional[datetime], Field(description="Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)")] = None,
        end_date: Annotated[Optional[datetime], Field(description="Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)")] = None,
        format: Annotated[Optional[StrictStr], Field(description="Output format: [JSON|CSV] Json is the default value")] = None,
        env: Annotated[Optional[StrictStr], Field(description="Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PagedEconomicDataDTO:
        """Returns the time series of values for different indicators.

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_economicdata_get\"  Indicator name as retrieved from /EconomicData/IndicatorList is mandatory.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

        :param indicator_name: Name of the indicator as found in /EconomicData/IndicatorList. (required)
        :type indicator_name: str
        :param page: Page number for paged results
        :type page: int
        :param iso3: The code to identify the country. Must be a ISO-3166 Alpha 3 code.
        :type iso3: str
        :param start_date: Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)
        :type start_date: datetime
        :param end_date: Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)
        :type end_date: datetime
        :param format: Output format: [JSON|CSV] Json is the default value
        :type format: str
        :param env: Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org
        :type env: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._economic_data_indicator_name_get_serialize(
            indicator_name=indicator_name,
            page=page,
            iso3=iso3,
            start_date=start_date,
            end_date=end_date,
            format=format,
            env=env,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PagedEconomicDataDTO",
            '400': "BadRequestDTO",
            '404': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def economic_data_indicator_name_get_with_http_info(
        self,
        indicator_name: Annotated[StrictStr, Field(description="Name of the indicator as found in /EconomicData/IndicatorList.")],
        page: Annotated[Optional[StrictInt], Field(description="Page number for paged results")] = None,
        iso3: Annotated[Optional[StrictStr], Field(description="The code to identify the country. Must be a ISO-3166 Alpha 3 code.")] = None,
        start_date: Annotated[Optional[datetime], Field(description="Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)")] = None,
        end_date: Annotated[Optional[datetime], Field(description="Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)")] = None,
        format: Annotated[Optional[StrictStr], Field(description="Output format: [JSON|CSV] Json is the default value")] = None,
        env: Annotated[Optional[StrictStr], Field(description="Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PagedEconomicDataDTO]:
        """Returns the time series of values for different indicators.

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_economicdata_get\"  Indicator name as retrieved from /EconomicData/IndicatorList is mandatory.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

        :param indicator_name: Name of the indicator as found in /EconomicData/IndicatorList. (required)
        :type indicator_name: str
        :param page: Page number for paged results
        :type page: int
        :param iso3: The code to identify the country. Must be a ISO-3166 Alpha 3 code.
        :type iso3: str
        :param start_date: Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)
        :type start_date: datetime
        :param end_date: Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)
        :type end_date: datetime
        :param format: Output format: [JSON|CSV] Json is the default value
        :type format: str
        :param env: Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org
        :type env: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._economic_data_indicator_name_get_serialize(
            indicator_name=indicator_name,
            page=page,
            iso3=iso3,
            start_date=start_date,
            end_date=end_date,
            format=format,
            env=env,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PagedEconomicDataDTO",
            '400': "BadRequestDTO",
            '404': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def economic_data_indicator_name_get_without_preload_content(
        self,
        indicator_name: Annotated[StrictStr, Field(description="Name of the indicator as found in /EconomicData/IndicatorList.")],
        page: Annotated[Optional[StrictInt], Field(description="Page number for paged results")] = None,
        iso3: Annotated[Optional[StrictStr], Field(description="The code to identify the country. Must be a ISO-3166 Alpha 3 code.")] = None,
        start_date: Annotated[Optional[datetime], Field(description="Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)")] = None,
        end_date: Annotated[Optional[datetime], Field(description="Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)")] = None,
        format: Annotated[Optional[StrictStr], Field(description="Output format: [JSON|CSV] Json is the default value")] = None,
        env: Annotated[Optional[StrictStr], Field(description="Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Returns the time series of values for different indicators.

          [![Generic badge](https://img.shields.io/badge/Maturity%20Level-Production%20Ready-green)]()  [![Generic badge](https://img.shields.io/badge/Access_Policy-TEC_Architecture_approval_required-yellow)]()  [![Generic badge](https://img.shields.io/badge/Data%20Classification-Public-green)]()  ### This endpoint is restricted, it requires the scope: \"vamdatabridges_economicdata_get\"  Indicator name as retrieved from /EconomicData/IndicatorList is mandatory.    **Data Controller** - Wael ATTIA  **API Integration Pattern** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern

        :param indicator_name: Name of the indicator as found in /EconomicData/IndicatorList. (required)
        :type indicator_name: str
        :param page: Page number for paged results
        :type page: int
        :param iso3: The code to identify the country. Must be a ISO-3166 Alpha 3 code.
        :type iso3: str
        :param start_date: Starting date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)
        :type start_date: datetime
        :param end_date: Ending date for the range in which data was collected. Use the date formats defined by RFC 3339 ; use strings matching year \\\"-\\\" month \\\"-\\\" day (e.g. 2020/06/24)
        :type end_date: datetime
        :param format: Output format: [JSON|CSV] Json is the default value
        :type format: str
        :param env: Environment.   * `prod` - api.vam.wfp.org   * `dev` - dev.api.vam.wfp.org
        :type env: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._economic_data_indicator_name_get_serialize(
            indicator_name=indicator_name,
            page=page,
            iso3=iso3,
            start_date=start_date,
            end_date=end_date,
            format=format,
            env=env,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PagedEconomicDataDTO",
            '400': "BadRequestDTO",
            '404': "ProblemDetails",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _economic_data_indicator_name_get_serialize(
        self,
        indicator_name,
        page,
        iso3,
        start_date,
        end_date,
        format,
        env,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, Union[str, bytes]] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if indicator_name is not None:
            _path_params['indicatorName'] = indicator_name
        # process the query parameters
        if page is not None:
            
            _query_params.append(('page', page))
            
        if iso3 is not None:
            
            _query_params.append(('iso3', iso3))
            
        if start_date is not None:
            if isinstance(start_date, datetime):
                _query_params.append(
                    (
                        'startDate',
                        start_date.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('startDate', start_date))
            
        if end_date is not None:
            if isinstance(end_date, datetime):
                _query_params.append(
                    (
                        'endDate',
                        end_date.strftime(
                            self.api_client.configuration.datetime_format
                        )
                    )
                )
            else:
                _query_params.append(('endDate', end_date))
            
        if format is not None:
            
            _query_params.append(('format', format))
            
        if env is not None:
            
            _query_params.append(('env', env))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'text/plain', 
                    'application/json', 
                    'text/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'default'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/EconomicData/{indicatorName}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


