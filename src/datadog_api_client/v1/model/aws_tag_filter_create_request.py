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
    from datadog_api_client.v1.model.aws_namespace import AWSNamespace


class AWSTagFilterCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.aws_namespace import AWSNamespace

        return {
            "account_id": (str,),
            "namespace": (AWSNamespace,),
            "tag_filter_str": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "namespace": "namespace",
        "tag_filter_str": "tag_filter_str",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        namespace: Union[AWSNamespace, UnsetType] = unset,
        tag_filter_str: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The objects used to set an AWS tag filter.

        :param account_id: Your AWS Account ID without dashes.
        :type account_id: str, optional

        :param namespace: The namespace associated with the tag filter entry.
        :type namespace: AWSNamespace, optional

        :param tag_filter_str: The tag filter string.
        :type tag_filter_str: str, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if namespace is not unset:
            kwargs["namespace"] = namespace
        if tag_filter_str is not unset:
            kwargs["tag_filter_str"] = tag_filter_str
        super().__init__(kwargs)
