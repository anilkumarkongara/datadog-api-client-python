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


class EventsRequestPage(ModelNormal):
    validations = {
        "limit": {
            "inclusive_maximum": 1000,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "cursor": (str,),
            "limit": (int,),
        }

    attribute_map = {
        "cursor": "cursor",
        "limit": "limit",
    }

    def __init__(self_, cursor: Union[str, UnsetType] = unset, limit: Union[int, UnsetType] = unset, **kwargs):
        """
        Pagination settings.

        :param cursor: The returned paging point to use to get the next results.
        :type cursor: str, optional

        :param limit: The maximum number of logs in the response.
        :type limit: int, optional
        """
        if cursor is not unset:
            kwargs["cursor"] = cursor
        if limit is not unset:
            kwargs["limit"] = limit
        super().__init__(kwargs)
