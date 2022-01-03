# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.list_stream_column import ListStreamColumn
    from datadog_api_client.v1.model.list_stream_query import ListStreamQuery
    from datadog_api_client.v1.model.list_stream_response_format import ListStreamResponseFormat

    globals()["ListStreamColumn"] = ListStreamColumn
    globals()["ListStreamQuery"] = ListStreamQuery
    globals()["ListStreamResponseFormat"] = ListStreamResponseFormat


class ListStreamWidgetRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "columns": ([ListStreamColumn],),
            "query": (ListStreamQuery,),
            "response_format": (ListStreamResponseFormat,),
        }

    attribute_map = {
        "columns": "columns",
        "query": "query",
        "response_format": "response_format",
    }

    read_only_vars = {}

    def __init__(self, columns, query, response_format, *args, **kwargs):
        """ListStreamWidgetRequest - a model defined in OpenAPI

        Args:
            columns ([ListStreamColumn]): Widget columns.
            query (ListStreamQuery):
            response_format (ListStreamResponseFormat):

        Keyword Args:
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.columns = columns
        self.query = query
        self.response_format = response_format

    @classmethod
    def _from_openapi_data(cls, columns, query, response_format, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ListStreamWidgetRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.columns = columns
        self.query = query
        self.response_format = response_format
        return self