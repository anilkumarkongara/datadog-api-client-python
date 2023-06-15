# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_service_create_data import IncidentServiceCreateData


@dataclass
class IncidentServiceCreateRequestJSON:
    name: Union[str, UnsetType] = unset
    created_by: Union[str, UnsetType] = unset
    last_modified_by: Union[str, UnsetType] = unset


class IncidentServiceCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_service_create_data import IncidentServiceCreateData

        return {
            "data": (IncidentServiceCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = IncidentServiceCreateRequestJSON

    def __init__(self_, data: IncidentServiceCreateData, **kwargs):
        """
        Create request with an incident service payload.

        :param data: Incident Service payload for create requests.
        :type data: IncidentServiceCreateData
        """
        super().__init__(kwargs)

        self_.data = data
