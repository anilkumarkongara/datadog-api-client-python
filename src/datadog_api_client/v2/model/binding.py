# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class Binding(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "principals": ([str],),
            "relation": (str,),
        }

    attribute_map = {
        "principals": "principals",
        "relation": "relation",
    }

    def __init__(self_, principals: List[str], relation: str, **kwargs):
        """
        Specifies which principals are associated with a relation.

        :param principals: An array of principals.
        :type principals: [str]

        :param relation: The role/level of access.
        :type relation: str
        """
        super().__init__(kwargs)

        self_.principals = principals
        self_.relation = relation
