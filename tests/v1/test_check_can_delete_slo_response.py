# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.check_can_delete_slo_response_data import CheckCanDeleteSLOResponseData

globals()["CheckCanDeleteSLOResponseData"] = CheckCanDeleteSLOResponseData
from datadog_api_client.v1.model.check_can_delete_slo_response import CheckCanDeleteSLOResponse


class TestCheckCanDeleteSLOResponse(unittest.TestCase):
    """CheckCanDeleteSLOResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCheckCanDeleteSLOResponse(self):
        """Test CheckCanDeleteSLOResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CheckCanDeleteSLOResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()