# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v1
from datadog_api_client.v1.model.usage_custom_reports_page import UsageCustomReportsPage

globals()["UsageCustomReportsPage"] = UsageCustomReportsPage
from datadog_api_client.v1.model.usage_custom_reports_meta import UsageCustomReportsMeta


class TestUsageCustomReportsMeta(unittest.TestCase):
    """UsageCustomReportsMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUsageCustomReportsMeta(self):
        """Test UsageCustomReportsMeta"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UsageCustomReportsMeta()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()