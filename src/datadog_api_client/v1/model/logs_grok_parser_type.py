# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelSimple,
    cached_property,
)


class LogsGrokParserType(ModelSimple):
    allowed_values = {
        "value": {
            "GROK_PARSER": "grok-parser",
        },
    }

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        Type of logs grok parser.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: If omitted defaults to "grok-parser". Must be one of ["grok-parser"].
        :type value: str
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            value = "grok-parser"

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
