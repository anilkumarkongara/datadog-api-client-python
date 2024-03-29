# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CIAppAggregateSortType(ModelSimple):
    """
    The type of sorting algorithm.

    :param value: If omitted defaults to "alphabetical". Must be one of ["alphabetical", "measure"].
    :type value: str
    """

    allowed_values = {
        "alphabetical",
        "measure",
    }
    ALPHABETICAL: ClassVar["CIAppAggregateSortType"]
    MEASURE: ClassVar["CIAppAggregateSortType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CIAppAggregateSortType.ALPHABETICAL = CIAppAggregateSortType("alphabetical")
CIAppAggregateSortType.MEASURE = CIAppAggregateSortType("measure")
