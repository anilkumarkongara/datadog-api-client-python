# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.application_key_update_data import ApplicationKeyUpdateData


@dataclass
class ApplicationKeyUpdateRequestJSON:
    id: str
    name: Union[str, UnsetType] = unset
    scopes: Union[List[str], none_type, UnsetType] = unset


class ApplicationKeyUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_key_update_data import ApplicationKeyUpdateData

        return {
            "data": (ApplicationKeyUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = ApplicationKeyUpdateRequestJSON

    def __init__(self_, data: ApplicationKeyUpdateData, **kwargs):
        """
        Request used to update an application key.

        :param data: Object used to update an application key.
        :type data: ApplicationKeyUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
