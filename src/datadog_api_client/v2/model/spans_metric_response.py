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


from datadog_api_client.v2.model.spans_metric_response_compute import SpansMetricResponseCompute
from datadog_api_client.v2.model.spans_metric_response_filter import SpansMetricResponseFilter
from datadog_api_client.v2.model.spans_metric_response_group_by import SpansMetricResponseGroupBy
from datadog_api_client.v2.model.spans_metric_response_compute import SpansMetricResponseCompute
from datadog_api_client.v2.model.spans_metric_response_filter import SpansMetricResponseFilter
from datadog_api_client.v2.model.spans_metric_response_group_by import SpansMetricResponseGroupBy

if TYPE_CHECKING:
    from datadog_api_client.v2.model.spans_metric_response_data import SpansMetricResponseData


@dataclass
class SpansMetricResponseJSON:
    id: str
    compute: Union[SpansMetricResponseCompute, UnsetType] = unset
    filter: Union[SpansMetricResponseFilter, UnsetType] = unset
    group_by: Union[List[SpansMetricResponseGroupBy], UnsetType] = unset


class SpansMetricResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_metric_response_data import SpansMetricResponseData

        return {
            "data": (SpansMetricResponseData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = SpansMetricResponseJSON

    def __init__(self_, data: Union[SpansMetricResponseData, UnsetType] = unset, **kwargs):
        """
        The span-based metric object.

        :param data: The span-based metric properties.
        :type data: SpansMetricResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
