# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.usage_specified_custom_reports_attributes import (
        UsageSpecifiedCustomReportsAttributes,
    )
    from datadog_api_client.v1.model.usage_reports_type import UsageReportsType


class UsageSpecifiedCustomReportsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_specified_custom_reports_attributes import (
            UsageSpecifiedCustomReportsAttributes,
        )
        from datadog_api_client.v1.model.usage_reports_type import UsageReportsType

        return {
            "attributes": (UsageSpecifiedCustomReportsAttributes,),
            "id": (str,),
            "type": (UsageReportsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[UsageSpecifiedCustomReportsAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[UsageReportsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing date and type for specified custom reports.

        :param attributes: The response containing attributes for specified custom reports.
        :type attributes: UsageSpecifiedCustomReportsAttributes, optional

        :param id: The date for specified custom reports.
        :type id: str, optional

        :param type: The type of reports.
        :type type: UsageReportsType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
