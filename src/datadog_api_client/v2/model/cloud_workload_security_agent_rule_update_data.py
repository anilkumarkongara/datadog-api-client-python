# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_attributes import (
        CloudWorkloadSecurityAgentRuleUpdateAttributes,
    )
    from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import CloudWorkloadSecurityAgentRuleType


class CloudWorkloadSecurityAgentRuleUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_update_attributes import (
            CloudWorkloadSecurityAgentRuleUpdateAttributes,
        )
        from datadog_api_client.v2.model.cloud_workload_security_agent_rule_type import (
            CloudWorkloadSecurityAgentRuleType,
        )

        return {
            "attributes": (CloudWorkloadSecurityAgentRuleUpdateAttributes,),
            "type": (CloudWorkloadSecurityAgentRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CloudWorkloadSecurityAgentRuleUpdateAttributes,
        type: CloudWorkloadSecurityAgentRuleType,
        **kwargs,
    ):
        """
        Object for a single Agent rule.

        :param attributes: Update an existing Cloud Workload Security Agent rule.
        :type attributes: CloudWorkloadSecurityAgentRuleUpdateAttributes

        :param type: The type of the resource. The value should always be ``agent_rule``.
        :type type: CloudWorkloadSecurityAgentRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
