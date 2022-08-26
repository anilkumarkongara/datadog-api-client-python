# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class OpsgenieServiceRegionType(ModelSimple):
    """
    The region for the Opsgenie service.

    :param value: Must be one of ["us", "eu", "custom"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "US": "us",
            "EU": "eu",
            "CUSTOM": "custom",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }