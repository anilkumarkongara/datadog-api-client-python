# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMApplicationListType(ModelSimple):
    """
    RUM application list type.

    :param value: If omitted defaults to "rum_application". Must be one of ["rum_application"].
    :type value: str
    """

    allowed_values = {
        "rum_application",
    }
    RUM_APPLICATION: ClassVar["RUMApplicationListType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMApplicationListType.RUM_APPLICATION = RUMApplicationListType("rum_application")
