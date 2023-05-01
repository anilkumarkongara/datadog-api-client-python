"""
Get the list of all Synthetic tests returns "OK - Returns the list of all Synthetic tests." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.list_tests()

    print(response)
