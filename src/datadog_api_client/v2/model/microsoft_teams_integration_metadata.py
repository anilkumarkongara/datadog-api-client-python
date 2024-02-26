# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.microsoft_teams_integration_metadata_teams_item import (
        MicrosoftTeamsIntegrationMetadataTeamsItem,
    )


class MicrosoftTeamsIntegrationMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.microsoft_teams_integration_metadata_teams_item import (
            MicrosoftTeamsIntegrationMetadataTeamsItem,
        )

        return {
            "teams": ([MicrosoftTeamsIntegrationMetadataTeamsItem],),
        }

    attribute_map = {
        "teams": "teams",
    }

    def __init__(self_, teams: List[MicrosoftTeamsIntegrationMetadataTeamsItem], **kwargs):
        """
        Incident integration metadata for the Microsoft Teams integration.

        :param teams: Array of Microsoft Teams teams in this integration metadata.
        :type teams: [MicrosoftTeamsIntegrationMetadataTeamsItem]
        """
        super().__init__(kwargs)

        self_.teams = teams
