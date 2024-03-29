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


class DashboardListDeleteResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "deleted_dashboard_list_id": (int,),
        }

    attribute_map = {
        "deleted_dashboard_list_id": "deleted_dashboard_list_id",
    }

    def __init__(self_, deleted_dashboard_list_id: Union[int, UnsetType] = unset, **kwargs):
        """
        Deleted dashboard details.

        :param deleted_dashboard_list_id: ID of the deleted dashboard list.
        :type deleted_dashboard_list_id: int, optional
        """
        if deleted_dashboard_list_id is not unset:
            kwargs["deleted_dashboard_list_id"] = deleted_dashboard_list_id
        super().__init__(kwargs)
