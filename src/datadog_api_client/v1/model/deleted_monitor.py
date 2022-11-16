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


class DeletedMonitor(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "deleted_monitor_id": (int,),
        }

    attribute_map = {
        "deleted_monitor_id": "deleted_monitor_id",
    }

    def __init__(self_, deleted_monitor_id: Union[int, UnsetType] = unset, **kwargs):
        """
        Response from the delete monitor call.

        :param deleted_monitor_id: ID of the deleted monitor.
        :type deleted_monitor_id: int, optional
        """
        if deleted_monitor_id is not unset:
            kwargs["deleted_monitor_id"] = deleted_monitor_id
        super().__init__(kwargs)
