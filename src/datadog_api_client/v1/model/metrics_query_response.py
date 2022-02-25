# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.metrics_query_metadata import MetricsQueryMetadata

    globals()["MetricsQueryMetadata"] = MetricsQueryMetadata


class MetricsQueryResponse(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "error": (str,),
            "from_date": (int,),
            "group_by": ([str],),
            "message": (str,),
            "query": (str,),
            "res_type": (str,),
            "series": ([MetricsQueryMetadata],),
            "status": (str,),
            "to_date": (int,),
        }

    attribute_map = {
        "error": "error",
        "from_date": "from_date",
        "group_by": "group_by",
        "message": "message",
        "query": "query",
        "res_type": "res_type",
        "series": "series",
        "status": "status",
        "to_date": "to_date",
    }

    read_only_vars = {
        "error",
        "from_date",
        "group_by",
        "message",
        "query",
        "res_type",
        "series",
        "status",
        "to_date",
    }

    def __init__(self, *args, **kwargs):
        """
        Response Object that includes your query and the list of metrics retrieved.

        :param error: Message indicating the errors if status is not `ok`.
        :type error: str, optional

        :param from_date: Start of requested time window, milliseconds since Unix epoch.
        :type from_date: int, optional

        :param group_by: List of tag keys on which to group.
        :type group_by: [str], optional

        :param message: Message indicating `success` if status is `ok`.
        :type message: str, optional

        :param query: Query string
        :type query: str, optional

        :param res_type: Type of response.
        :type res_type: str, optional

        :param series: List of timeseries queried.
        :type series: [MetricsQueryMetadata], optional

        :param status: Status of the query.
        :type status: str, optional

        :param to_date: End of requested time window, milliseconds since Unix epoch.
        :type to_date: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MetricsQueryResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
