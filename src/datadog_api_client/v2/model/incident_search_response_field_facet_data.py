# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class IncidentSearchResponseFieldFacetData(ModelNormal):
    validations = {
        "count": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "name": (str,),
        }

    attribute_map = {
        "count": "count",
        "name": "name",
    }

    def __init__(self_, count: Union[int, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Facet value and number of occurrences for a property field of an incident.

        :param count: Count of the facet value appearing in search results.
        :type count: int, optional

        :param name: The facet value appearing in search results.
        :type name: str, optional
        """
        if count is not unset:
            kwargs["count"] = count
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
