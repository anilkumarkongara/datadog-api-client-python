# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.aws_tag_filter import AWSTagFilter

    globals()["AWSTagFilter"] = AWSTagFilter


class AWSTagFilterListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "filters": ([AWSTagFilter],),
        }

    attribute_map = {
        "filters": "filters",
    }

    def __init__(self, *args, **kwargs):
        """
        An array of tag filter rules by ``namespace`` and tag filter string.

        :param filters: An array of tag filters.
        :type filters: [AWSTagFilter], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(AWSTagFilterListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
