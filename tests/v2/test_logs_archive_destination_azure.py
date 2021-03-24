# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.logs_archive_destination_azure_type import LogsArchiveDestinationAzureType
from datadog_api_client.v2.model.logs_archive_integration_azure import LogsArchiveIntegrationAzure

globals()["LogsArchiveDestinationAzureType"] = LogsArchiveDestinationAzureType
globals()["LogsArchiveIntegrationAzure"] = LogsArchiveIntegrationAzure
from datadog_api_client.v2.model.logs_archive_destination_azure import LogsArchiveDestinationAzure


class TestLogsArchiveDestinationAzure(unittest.TestCase):
    """LogsArchiveDestinationAzure unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogsArchiveDestinationAzure(self):
        """Test LogsArchiveDestinationAzure"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogsArchiveDestinationAzure()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()