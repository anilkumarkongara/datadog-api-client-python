# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.ip_allowlist_entry import IPAllowlistEntry
from datadog_api_client.v2.model.ip_allowlist_entry import IPAllowlistEntry

if TYPE_CHECKING:
    from datadog_api_client.v2.model.ip_allowlist_data import IPAllowlistData


@dataclass
class IPAllowlistResponseJSON:
    id: str
    enabled: Union[bool, UnsetType] = unset
    entries: Union[List[IPAllowlistEntry], UnsetType] = unset


class IPAllowlistResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ip_allowlist_data import IPAllowlistData

        return {
            "data": (IPAllowlistData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = IPAllowlistResponseJSON

    def __init__(self_, data: Union[IPAllowlistData, UnsetType] = unset, **kwargs):
        """
        Response containing information about the IP allowlist.

        :param data: IP allowlist data.
        :type data: IPAllowlistData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
