# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class AuthNMappingsType(ModelSimple):
    """
    AuthN Mappings resource type.

    :param value: If omitted defaults to "authn_mappings". Must be one of ["authn_mappings"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "AUTHN_MAPPINGS": "authn_mappings",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }