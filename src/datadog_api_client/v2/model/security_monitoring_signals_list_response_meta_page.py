# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalsListResponseMetaPage(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "after": (str,),
        }

    attribute_map = {
        "after": "after",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Paging attributes.

        :param after: The cursor used to get the next results, if any. To make the next request, use the same
            parameters with the addition of the `page[cursor]`.
        :type after: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringSignalsListResponseMetaPage, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
