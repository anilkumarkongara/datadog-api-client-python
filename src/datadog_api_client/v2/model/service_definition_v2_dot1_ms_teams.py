# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_definition_v2_dot1_ms_teams_type import ServiceDefinitionV2Dot1MSTeamsType


class ServiceDefinitionV2Dot1MSTeams(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_definition_v2_dot1_ms_teams_type import (
            ServiceDefinitionV2Dot1MSTeamsType,
        )

        return {
            "contact": (str,),
            "name": (str,),
            "type": (ServiceDefinitionV2Dot1MSTeamsType,),
        }

    attribute_map = {
        "contact": "contact",
        "name": "name",
        "type": "type",
    }

    def __init__(
        self_, contact: str, type: ServiceDefinitionV2Dot1MSTeamsType, name: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Service owner's Microsoft Teams.

        :param contact: Contact value.
        :type contact: str

        :param name: Contact Microsoft Teams.
        :type name: str, optional

        :param type: Contact type.
        :type type: ServiceDefinitionV2Dot1MSTeamsType
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.contact = contact
        self_.type = type
