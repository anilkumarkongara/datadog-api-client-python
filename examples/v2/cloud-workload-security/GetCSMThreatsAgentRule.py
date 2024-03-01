"""
Get a CSM Threats Agent rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_workload_security_api import CloudWorkloadSecurityApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudWorkloadSecurityApi(api_client)
    response = api_instance.get_csm_threats_agent_rule(
        agent_rule_id="agent_rule_id",
    )

    print(response)
