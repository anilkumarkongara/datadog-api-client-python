# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class MetricBulkTagConfigTagNameList(ModelSimple):
    """
    A list of tag names to apply to the configuration.


    :type value: [str]
    """

    @cached_property
    def openapi_types(_):
        return {
            "value": ([str],),
        }