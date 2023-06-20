"""
Edit an app key owned by this service account returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_accounts_api import ServiceAccountsApi
from datadog_api_client.v2.model.application_key_update_request import ApplicationKeyUpdateRequestJSON

# there is a valid "service_account_user" in the system
SERVICE_ACCOUNT_USER_DATA_ID = environ["SERVICE_ACCOUNT_USER_DATA_ID"]

# there is a valid "service_account_application_key" for "service_account_user"
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ATTRIBUTES_NAME = environ["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ATTRIBUTES_NAME"]
SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID = environ["SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID"]

body = ApplicationKeyUpdateRequestJSON(
    name="Application Key for managing dashboards-updated",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceAccountsApi(api_client)
    response = api_instance.update_service_account_application_key(
        service_account_id=SERVICE_ACCOUNT_USER_DATA_ID, app_key_id=SERVICE_ACCOUNT_APPLICATION_KEY_DATA_ID, body=body
    )

    print(response)
