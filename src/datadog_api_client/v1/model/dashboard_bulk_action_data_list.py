# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class DashboardBulkActionDataList(ModelSimple):
    """
    List of dashboard bulk action request data objects.


    :type value: [DashboardBulkActionData]
    """

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dashboard_bulk_action_data import DashboardBulkActionData

        return {
            "value": ([DashboardBulkActionData],),
        }
