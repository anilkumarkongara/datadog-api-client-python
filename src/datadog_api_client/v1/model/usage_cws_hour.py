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


class UsageCWSHour(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "cws_container_count": (int,),
            "cws_host_count": (int,),
            "hour": (datetime,),
            "org_name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "cws_container_count": "cws_container_count",
        "cws_host_count": "cws_host_count",
        "hour": "hour",
        "org_name": "org_name",
        "public_id": "public_id",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """UsageCWSHour - a model defined in OpenAPI

        Keyword Args:
            cws_container_count (int): [optional] The total number of Cloud Workload Security container hours from the start of the given hour’s month until the given hour.
            cws_host_count (int): [optional] The total number of Cloud Workload Security host hours from the start of the given hour’s month until the given hour.
            hour (datetime): [optional] The hour for the usage.
            org_name (str): [optional] The organization name.
            public_id (str): [optional] The organization public ID.
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageCWSHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self