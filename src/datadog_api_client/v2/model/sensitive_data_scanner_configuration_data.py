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
    from datadog_api_client.v2.model.sensitive_data_scanner_configuration import SensitiveDataScannerConfiguration


class SensitiveDataScannerConfigurationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_configuration import SensitiveDataScannerConfiguration

        return {
            "data": (SensitiveDataScannerConfiguration,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[SensitiveDataScannerConfiguration, UnsetType] = unset, **kwargs):
        """
        A Sensitive Data Scanner configuration data.

        :param data: A Sensitive Data Scanner configuration.
        :type data: SensitiveDataScannerConfiguration, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
