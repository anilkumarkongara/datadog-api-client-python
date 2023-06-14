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


from datadog_api_client.v2.model.application_key_create_attributes import ApplicationKeyCreateAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType


@dataclass
class ApplicationKeyCreateDataJSON:
    name: Union[str, UnsetType] = unset
    scopes: Union[List[str], none_type, UnsetType] = unset


class ApplicationKeyCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_keys_type import ApplicationKeysType

        return {
            "attributes": (ApplicationKeyCreateAttributes,),
            "type": (ApplicationKeysType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = ApplicationKeyCreateDataJSON

    def __init__(self_, attributes: ApplicationKeyCreateAttributes, type: ApplicationKeysType, **kwargs):
        """
        Object used to create an application key.

        :param attributes: Attributes used to create an application Key.
        :type attributes: ApplicationKeyCreateAttributes

        :param type: Application Keys resource type.
        :type type: ApplicationKeysType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
