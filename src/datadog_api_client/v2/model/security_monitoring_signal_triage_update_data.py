# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityMonitoringSignalTriageUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_signal_triage_attributes import (
            SecurityMonitoringSignalTriageAttributes,
        )

        return {
            "attributes": (SecurityMonitoringSignalTriageAttributes,),
        }

    attribute_map = {
        "attributes": "attributes",
    }

    def __init__(self, *args, **kwargs):
        """
        Data containing the updated triage attributes of the signal.

        :param attributes: Attributes describing a triage state update operation over a security signal.
        :type attributes: SecurityMonitoringSignalTriageAttributes, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SecurityMonitoringSignalTriageUpdateData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self