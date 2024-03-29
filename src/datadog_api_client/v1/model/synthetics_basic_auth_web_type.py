# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsBasicAuthWebType(ModelSimple):
    """
    The type of basic authentication to use when performing the test.

    :param value: If omitted defaults to "web". Must be one of ["web"].
    :type value: str
    """

    allowed_values = {
        "web",
    }
    WEB: ClassVar["SyntheticsBasicAuthWebType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsBasicAuthWebType.WEB = SyntheticsBasicAuthWebType("web")
