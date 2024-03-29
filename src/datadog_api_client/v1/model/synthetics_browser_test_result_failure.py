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
    from datadog_api_client.v1.model.synthetics_browser_test_failure_code import SyntheticsBrowserTestFailureCode


class SyntheticsBrowserTestResultFailure(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_browser_test_failure_code import SyntheticsBrowserTestFailureCode

        return {
            "code": (SyntheticsBrowserTestFailureCode,),
            "message": (str,),
        }

    attribute_map = {
        "code": "code",
        "message": "message",
    }

    def __init__(
        self_,
        code: Union[SyntheticsBrowserTestFailureCode, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The browser test failure details.

        :param code: Error code that can be returned by a Synthetic test.
        :type code: SyntheticsBrowserTestFailureCode, optional

        :param message: The browser test error message.
        :type message: str, optional
        """
        if code is not unset:
            kwargs["code"] = code
        if message is not unset:
            kwargs["message"] = message
        super().__init__(kwargs)
