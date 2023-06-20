"""
Update an existing incident integration metadata returns "OK" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_integration_metadata_patch_request import (
    IncidentIntegrationMetadataPatchRequestJSON,
)
from datadog_api_client.v2.model.slack_integration_metadata import SlackIntegrationMetadata
from datadog_api_client.v2.model.slack_integration_metadata_channel_item import SlackIntegrationMetadataChannelItem

# there is a valid "incident" in the system
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

# the "incident" has an "incident_integration_metadata"
INCIDENT_INTEGRATION_METADATA_DATA_ID = environ["INCIDENT_INTEGRATION_METADATA_DATA_ID"]

body = IncidentIntegrationMetadataPatchRequestJSON(
    incident_id=INCIDENT_DATA_ID,
    integration_type=1,
    metadata=SlackIntegrationMetadata(
        channels=[
            SlackIntegrationMetadataChannelItem(
                channel_id="C0123456789",
                channel_name="#updated-channel-name",
                team_id="T01234567",
                redirect_url="https://slack.com/app_redirect?channel=C0123456789&team=T01234567",
            ),
        ],
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_integration"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_integration(
        incident_id=INCIDENT_DATA_ID, integration_metadata_id=INCIDENT_INTEGRATION_METADATA_DATA_ID, body=body
    )

    print(response)
