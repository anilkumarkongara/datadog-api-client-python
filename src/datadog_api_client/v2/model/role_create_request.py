# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.role_create_data import RoleCreateData


@dataclass
class RoleCreateRequestJSON:
    created_at: Union[datetime, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    permissions: Union[List[str], UnsetType] = unset
    users: Union[List[str], UnsetType] = unset


class RoleCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.role_create_data import RoleCreateData

        return {
            "data": (RoleCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = RoleCreateRequestJSON

    def __init__(self_, data: RoleCreateData, **kwargs):
        """
        Create a role.

        :param data: Data related to the creation of a role.
        :type data: RoleCreateData
        """
        super().__init__(kwargs)

        self_.data = data
