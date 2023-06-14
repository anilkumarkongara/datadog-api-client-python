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


from datadog_api_client.v2.model.user_create_attributes import UserCreateAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.user_relationships import UserRelationships
    from datadog_api_client.v2.model.users_type import UsersType


@dataclass
class UserCreateDataJSON:
    email: Union[str, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    title: Union[str, UnsetType] = unset
    roles: Union[List[str], UnsetType] = unset


class UserCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.user_relationships import UserRelationships
        from datadog_api_client.v2.model.users_type import UsersType

        return {
            "attributes": (UserCreateAttributes,),
            "relationships": (UserRelationships,),
            "type": (UsersType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }
    json_api_model = UserCreateDataJSON

    def __init__(
        self_,
        attributes: UserCreateAttributes,
        type: UsersType,
        relationships: Union[UserRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object to create a user.

        :param attributes: Attributes of the created user.
        :type attributes: UserCreateAttributes

        :param relationships: Relationships of the user object.
        :type relationships: UserRelationships, optional

        :param type: Users resource type.
        :type type: UsersType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
