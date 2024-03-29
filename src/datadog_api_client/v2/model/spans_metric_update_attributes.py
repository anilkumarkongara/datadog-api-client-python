# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.spans_metric_update_compute import SpansMetricUpdateCompute
    from datadog_api_client.v2.model.spans_metric_filter import SpansMetricFilter
    from datadog_api_client.v2.model.spans_metric_group_by import SpansMetricGroupBy


class SpansMetricUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_metric_update_compute import SpansMetricUpdateCompute
        from datadog_api_client.v2.model.spans_metric_filter import SpansMetricFilter
        from datadog_api_client.v2.model.spans_metric_group_by import SpansMetricGroupBy

        return {
            "compute": (SpansMetricUpdateCompute,),
            "filter": (SpansMetricFilter,),
            "group_by": ([SpansMetricGroupBy],),
        }

    attribute_map = {
        "compute": "compute",
        "filter": "filter",
        "group_by": "group_by",
    }

    def __init__(
        self_,
        compute: Union[SpansMetricUpdateCompute, UnsetType] = unset,
        filter: Union[SpansMetricFilter, UnsetType] = unset,
        group_by: Union[List[SpansMetricGroupBy], UnsetType] = unset,
        **kwargs,
    ):
        """
        The span-based metric properties that will be updated.

        :param compute: The compute rule to compute the span-based metric.
        :type compute: SpansMetricUpdateCompute, optional

        :param filter: The span-based metric filter. Spans matching this filter will be aggregated in this metric.
        :type filter: SpansMetricFilter, optional

        :param group_by: The rules for the group by.
        :type group_by: [SpansMetricGroupBy], optional
        """
        if compute is not unset:
            kwargs["compute"] = compute
        if filter is not unset:
            kwargs["filter"] = filter
        if group_by is not unset:
            kwargs["group_by"] = group_by
        super().__init__(kwargs)
