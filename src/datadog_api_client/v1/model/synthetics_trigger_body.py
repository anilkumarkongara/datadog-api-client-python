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
    from datadog_api_client.v1.model.synthetics_trigger_test import SyntheticsTriggerTest

    globals()["SyntheticsTriggerTest"] = SyntheticsTriggerTest


class SyntheticsTriggerBody(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "tests": ([SyntheticsTriggerTest],),
        }

    attribute_map = {
        "tests": "tests",
    }

    read_only_vars = {}

    def __init__(self, tests, *args, **kwargs):
        """SyntheticsTriggerBody - a model defined in OpenAPI

        Args:
            tests ([SyntheticsTriggerTest]): Individual synthetics test.

        Keyword Args:
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.tests = tests

    @classmethod
    def _from_openapi_data(cls, tests, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTriggerBody, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.tests = tests
        return self