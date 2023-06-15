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


from datadog_api_client.v2.model.monitor_config_policy_policy import MonitorConfigPolicyPolicy
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType
from datadog_api_client.v2.model.monitor_config_policy_policy import MonitorConfigPolicyPolicy
from datadog_api_client.v2.model.monitor_config_policy_tag_policy import MonitorConfigPolicyTagPolicy
from datadog_api_client.v2.model.monitor_config_policy_type import MonitorConfigPolicyType

if TYPE_CHECKING:
    from datadog_api_client.v2.model.monitor_config_policy_edit_data import MonitorConfigPolicyEditData


@dataclass
class MonitorConfigPolicyEditRequestJSON:
    id: str
    policy: Union[MonitorConfigPolicyPolicy, MonitorConfigPolicyTagPolicy, UnsetType] = unset
    policy_type: Union[MonitorConfigPolicyType, UnsetType] = unset


class MonitorConfigPolicyEditRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.monitor_config_policy_edit_data import MonitorConfigPolicyEditData

        return {
            "data": (MonitorConfigPolicyEditData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = MonitorConfigPolicyEditRequestJSON

    def __init__(self_, data: MonitorConfigPolicyEditData, **kwargs):
        """
        Request for editing a monitor configuration policy.

        :param data: A monitor configuration policy data.
        :type data: MonitorConfigPolicyEditData
        """
        super().__init__(kwargs)

        self_.data = data
