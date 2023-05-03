"""
    VAM-Data-Bridges

    API Documentation of the **DataBridges** platform: https://databridges.vam.wfp.org/. For API discussions and details: #api-integration-vam-data-bridges on Slack, [Teams channel](https://teams.microsoft.com/l/team/19%3a4ca595f7681f4ffa8a86b7af58832e8d%40thread.skype/conversations?groupId=cbd1e508-c6e8-459d-96b7-6cac3039c42c&tenantId=462ad9ae-d7d9-4206-b874-71b1e079776f) **API Integration** - This endpoint uses [Hey Jude](https://docs.api.wfp.org/providers/#api-patterns) pattern  # noqa: E501

    The version of the OpenAPI document: 1.3.1
    Contact: wfp.economicanalysis@wfp.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import data_bridges_client
from data_bridges_client.model.coordinate_equality_comparer import CoordinateEqualityComparer
from data_bridges_client.model.coordinate_sequence_factory import CoordinateSequenceFactory
from data_bridges_client.model.geometry_overlay import GeometryOverlay
from data_bridges_client.model.precision_model import PrecisionModel
globals()['CoordinateEqualityComparer'] = CoordinateEqualityComparer
globals()['CoordinateSequenceFactory'] = CoordinateSequenceFactory
globals()['GeometryOverlay'] = GeometryOverlay
globals()['PrecisionModel'] = PrecisionModel
from data_bridges_client.model.nts_geometry_services import NtsGeometryServices


class TestNtsGeometryServices(unittest.TestCase):
    """NtsGeometryServices unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNtsGeometryServices(self):
        """Test NtsGeometryServices"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NtsGeometryServices()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()