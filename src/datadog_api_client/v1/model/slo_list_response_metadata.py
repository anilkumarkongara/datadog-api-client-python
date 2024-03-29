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
    from datadog_api_client.v1.model.slo_list_response_metadata_page import SLOListResponseMetadataPage


class SLOListResponseMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_list_response_metadata_page import SLOListResponseMetadataPage

        return {
            "page": (SLOListResponseMetadataPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[SLOListResponseMetadataPage, UnsetType] = unset, **kwargs):
        """
        The metadata object containing additional information about the list of SLOs.

        :param page: The object containing information about the pages of the list of SLOs.
        :type page: SLOListResponseMetadataPage, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
