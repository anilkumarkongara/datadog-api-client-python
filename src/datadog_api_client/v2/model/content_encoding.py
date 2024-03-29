# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ContentEncoding(ModelSimple):
    """
    HTTP header used to compress the media-type.

    :param value: Must be one of ["identity", "gzip", "deflate"].
    :type value: str
    """

    allowed_values = {
        "identity",
        "gzip",
        "deflate",
    }
    IDENTITY: ClassVar["ContentEncoding"]
    GZIP: ClassVar["ContentEncoding"]
    DEFLATE: ClassVar["ContentEncoding"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ContentEncoding.IDENTITY = ContentEncoding("identity")
ContentEncoding.GZIP = ContentEncoding("gzip")
ContentEncoding.DEFLATE = ContentEncoding("deflate")
