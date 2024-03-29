# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class APIErrorResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "errors": ([str],),
        }

    attribute_map = {
        "errors": "errors",
    }

    def __init__(self_, errors: List[str], **kwargs):
        """
        Error response object.

        :param errors: Array of errors returned by the API.
        :type errors: [str]
        """
        super().__init__(kwargs)

        self_.errors = errors
