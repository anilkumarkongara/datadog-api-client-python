# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.usage_synthetics_hour import UsageSyntheticsHour

    globals()["UsageSyntheticsHour"] = UsageSyntheticsHour


class UsageSyntheticsResponse(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "usage": ([UsageSyntheticsHour],),
        }

    attribute_map = {
        "usage": "usage",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Response containing the number of Synthetics API tests run for each hour for a given organization.

        :param usage: Array with the number of hourly Synthetics test run for a given organization.
        :type usage: [UsageSyntheticsHour], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageSyntheticsResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
