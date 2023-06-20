"""
Create an application key for this service account returns "Created" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.application_key_create_request import ApplicationKeyCreateRequestJSON

body = ApplicationKeyCreateRequestJSON(
    name="Application Key for managing dashboards",
    scopes=[
        "dashboards_read",
        "dashboards_write",
        "dashboards_public_share",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.create_service_account_application_key(
        service_account_id="00000000-0000-1234-0000-000000000000", body=body
    )

    print(response)
