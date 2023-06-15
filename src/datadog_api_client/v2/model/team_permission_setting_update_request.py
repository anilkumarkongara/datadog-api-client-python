# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.team_permission_setting_value import TeamPermissionSettingValue
from datadog_api_client.v2.model.team_permission_setting_value import TeamPermissionSettingValue

if TYPE_CHECKING:
    from datadog_api_client.v2.model.team_permission_setting_update import TeamPermissionSettingUpdate


@dataclass
class TeamPermissionSettingUpdateRequestJSON:
    value: Union[TeamPermissionSettingValue, UnsetType] = unset


class TeamPermissionSettingUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.team_permission_setting_update import TeamPermissionSettingUpdate

        return {
            "data": (TeamPermissionSettingUpdate,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = TeamPermissionSettingUpdateRequestJSON

    def __init__(self_, data: TeamPermissionSettingUpdate, **kwargs):
        """
        Team permission setting update request

        :param data: Team permission setting update
        :type data: TeamPermissionSettingUpdate
        """
        super().__init__(kwargs)

        self_.data = data
