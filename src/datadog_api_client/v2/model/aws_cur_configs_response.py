# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_cur_config import AwsCURConfig


class AwsCURConfigsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_cur_config import AwsCURConfig

        return {
            "data": ([AwsCURConfig],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[AwsCURConfig], UnsetType] = unset, **kwargs):
        """
        List of AWS CUR configs.

        :param data: An AWS CUR config.
        :type data: [AwsCURConfig], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
