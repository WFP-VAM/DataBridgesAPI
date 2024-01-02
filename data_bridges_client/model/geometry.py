"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: wfp.economicanalysis@wfp.org
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from data_bridges_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from data_bridges_client.exceptions import ApiAttributeError


def lazy_import():
    from data_bridges_client.model.coordinate import Coordinate
    from data_bridges_client.model.dimension import Dimension
    from data_bridges_client.model.envelope import Envelope
    from data_bridges_client.model.geometry_factory import GeometryFactory
    from data_bridges_client.model.ogc_geometry_type import OgcGeometryType
    from data_bridges_client.model.point import Point
    from data_bridges_client.model.precision_model import PrecisionModel
    globals()['Coordinate'] = Coordinate
    globals()['Dimension'] = Dimension
    globals()['Envelope'] = Envelope
    globals()['GeometryFactory'] = GeometryFactory
    globals()['OgcGeometryType'] = OgcGeometryType
    globals()['Point'] = Point
    globals()['PrecisionModel'] = PrecisionModel


class Geometry(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'factory': (GeometryFactory,),  # noqa: E501
            'user_data': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'srid': (int,),  # noqa: E501
            'geometry_type': (str, none_type,),  # noqa: E501
            'ogc_geometry_type': (OgcGeometryType,),  # noqa: E501
            'precision_model': (PrecisionModel,),  # noqa: E501
            'coordinate': (Coordinate,),  # noqa: E501
            'coordinates': ([Coordinate], none_type,),  # noqa: E501
            'num_points': (int,),  # noqa: E501
            'num_geometries': (int,),  # noqa: E501
            'is_simple': (bool,),  # noqa: E501
            'is_valid': (bool,),  # noqa: E501
            'is_empty': (bool,),  # noqa: E501
            'area': (float,),  # noqa: E501
            'length': (float,),  # noqa: E501
            'centroid': (Point,),  # noqa: E501
            'interior_point': (Point,),  # noqa: E501
            'point_on_surface': (Point,),  # noqa: E501
            'dimension': (Dimension,),  # noqa: E501
            'boundary': (Geometry,),  # noqa: E501
            'boundary_dimension': (Dimension,),  # noqa: E501
            'envelope': (Geometry,),  # noqa: E501
            'envelope_internal': (Envelope,),  # noqa: E501
            'is_rectangle': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'factory': 'factory',  # noqa: E501
        'user_data': 'userData',  # noqa: E501
        'srid': 'srid',  # noqa: E501
        'geometry_type': 'geometryType',  # noqa: E501
        'ogc_geometry_type': 'ogcGeometryType',  # noqa: E501
        'precision_model': 'precisionModel',  # noqa: E501
        'coordinate': 'coordinate',  # noqa: E501
        'coordinates': 'coordinates',  # noqa: E501
        'num_points': 'numPoints',  # noqa: E501
        'num_geometries': 'numGeometries',  # noqa: E501
        'is_simple': 'isSimple',  # noqa: E501
        'is_valid': 'isValid',  # noqa: E501
        'is_empty': 'isEmpty',  # noqa: E501
        'area': 'area',  # noqa: E501
        'length': 'length',  # noqa: E501
        'centroid': 'centroid',  # noqa: E501
        'interior_point': 'interiorPoint',  # noqa: E501
        'point_on_surface': 'pointOnSurface',  # noqa: E501
        'dimension': 'dimension',  # noqa: E501
        'boundary': 'boundary',  # noqa: E501
        'boundary_dimension': 'boundaryDimension',  # noqa: E501
        'envelope': 'envelope',  # noqa: E501
        'envelope_internal': 'envelopeInternal',  # noqa: E501
        'is_rectangle': 'isRectangle',  # noqa: E501
    }

    read_only_vars = {
        'geometry_type',  # noqa: E501
        'coordinates',  # noqa: E501
        'num_points',  # noqa: E501
        'num_geometries',  # noqa: E501
        'is_simple',  # noqa: E501
        'is_valid',  # noqa: E501
        'is_empty',  # noqa: E501
        'area',  # noqa: E501
        'length',  # noqa: E501
        'is_rectangle',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Geometry - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            factory (GeometryFactory): [optional]  # noqa: E501
            user_data (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            srid (int): [optional]  # noqa: E501
            geometry_type (str, none_type): [optional]  # noqa: E501
            ogc_geometry_type (OgcGeometryType): [optional]  # noqa: E501
            precision_model (PrecisionModel): [optional]  # noqa: E501
            coordinate (Coordinate): [optional]  # noqa: E501
            coordinates ([Coordinate], none_type): [optional]  # noqa: E501
            num_points (int): [optional]  # noqa: E501
            num_geometries (int): [optional]  # noqa: E501
            is_simple (bool): [optional]  # noqa: E501
            is_valid (bool): [optional]  # noqa: E501
            is_empty (bool): [optional]  # noqa: E501
            area (float): [optional]  # noqa: E501
            length (float): [optional]  # noqa: E501
            centroid (Point): [optional]  # noqa: E501
            interior_point (Point): [optional]  # noqa: E501
            point_on_surface (Point): [optional]  # noqa: E501
            dimension (Dimension): [optional]  # noqa: E501
            boundary (Geometry): [optional]  # noqa: E501
            boundary_dimension (Dimension): [optional]  # noqa: E501
            envelope (Geometry): [optional]  # noqa: E501
            envelope_internal (Envelope): [optional]  # noqa: E501
            is_rectangle (bool): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Geometry - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            factory (GeometryFactory): [optional]  # noqa: E501
            user_data (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            srid (int): [optional]  # noqa: E501
            geometry_type (str, none_type): [optional]  # noqa: E501
            ogc_geometry_type (OgcGeometryType): [optional]  # noqa: E501
            precision_model (PrecisionModel): [optional]  # noqa: E501
            coordinate (Coordinate): [optional]  # noqa: E501
            coordinates ([Coordinate], none_type): [optional]  # noqa: E501
            num_points (int): [optional]  # noqa: E501
            num_geometries (int): [optional]  # noqa: E501
            is_simple (bool): [optional]  # noqa: E501
            is_valid (bool): [optional]  # noqa: E501
            is_empty (bool): [optional]  # noqa: E501
            area (float): [optional]  # noqa: E501
            length (float): [optional]  # noqa: E501
            centroid (Point): [optional]  # noqa: E501
            interior_point (Point): [optional]  # noqa: E501
            point_on_surface (Point): [optional]  # noqa: E501
            dimension (Dimension): [optional]  # noqa: E501
            boundary (Geometry): [optional]  # noqa: E501
            boundary_dimension (Dimension): [optional]  # noqa: E501
            envelope (Geometry): [optional]  # noqa: E501
            envelope_internal (Envelope): [optional]  # noqa: E501
            is_rectangle (bool): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
