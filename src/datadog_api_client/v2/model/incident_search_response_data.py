# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.incident_search_response_facets_data import IncidentSearchResponseFacetsData
from datadog_api_client.v2.model.incident_search_response_incidents_data import IncidentSearchResponseIncidentsData
from datadog_api_client.v2.model.incident_search_response_attributes import IncidentSearchResponseAttributes
from datadog_api_client.v2.model.incident_search_response_facets_data import IncidentSearchResponseFacetsData
from datadog_api_client.v2.model.incident_search_response_incidents_data import IncidentSearchResponseIncidentsData

if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_search_results_type import IncidentSearchResultsType


@dataclass
class IncidentSearchResponseDataJSON:
    facets: Union[IncidentSearchResponseFacetsData, UnsetType] = unset
    incidents: Union[List[IncidentSearchResponseIncidentsData], UnsetType] = unset
    total: Union[int, UnsetType] = unset


class IncidentSearchResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_search_results_type import IncidentSearchResultsType

        return {
            "attributes": (IncidentSearchResponseAttributes,),
            "type": (IncidentSearchResultsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = IncidentSearchResponseDataJSON

    def __init__(
        self_,
        attributes: Union[IncidentSearchResponseAttributes, UnsetType] = unset,
        type: Union[IncidentSearchResultsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data returned by an incident search.

        :param attributes: Attributes returned by an incident search.
        :type attributes: IncidentSearchResponseAttributes, optional

        :param type: Incident search result type.
        :type type: IncidentSearchResultsType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
