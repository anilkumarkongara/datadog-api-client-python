# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentTimelineCellMarkdownContentType(ModelSimple):
    """
    Type of the Markdown timeline cell.

    :param value: If omitted defaults to "markdown". Must be one of ["markdown"].
    :type value: str
    """

    allowed_values = {
        "markdown",
    }
    MARKDOWN: ClassVar["IncidentTimelineCellMarkdownContentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentTimelineCellMarkdownContentType.MARKDOWN = IncidentTimelineCellMarkdownContentType("markdown")
