# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
)


class UsageSummaryDateOrg(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            "agent_host_top99p": (int,),  # noqa: E501
            "apm_azure_app_service_host_top99p": (int,),  # noqa: E501
            "apm_host_top99p": (int,),  # noqa: E501
            "audit_logs_lines_indexed_sum": (int,),  # noqa: E501
            "aws_host_top99p": (int,),  # noqa: E501
            "aws_lambda_func_count": (int,),  # noqa: E501
            "aws_lambda_invocations_sum": (int,),  # noqa: E501
            "azure_app_service_top99p": (int,),  # noqa: E501
            "billable_ingested_bytes_sum": (int,),  # noqa: E501
            "container_avg": (int,),  # noqa: E501
            "container_hwm": (int,),  # noqa: E501
            "cspm_container_avg": (int,),  # noqa: E501
            "cspm_container_hwm": (int,),  # noqa: E501
            "cspm_host_top99p": (int,),  # noqa: E501
            "custom_ts_avg": (int,),  # noqa: E501
            "cws_container_count_avg": (int,),  # noqa: E501
            "cws_host_top99p": (int,),  # noqa: E501
            "dbm_host_top99p_sum": (int,),  # noqa: E501
            "dbm_queries_avg_sum": (int,),  # noqa: E501
            "fargate_tasks_count_avg": (int,),  # noqa: E501
            "fargate_tasks_count_hwm": (int,),  # noqa: E501
            "gcp_host_top99p": (int,),  # noqa: E501
            "heroku_host_top99p": (int,),  # noqa: E501
            "id": (str,),  # noqa: E501
            "incident_management_monthly_active_users_hwm": (int,),  # noqa: E501
            "indexed_events_count_sum": (int,),  # noqa: E501
            "infra_host_top99p": (int,),  # noqa: E501
            "ingested_events_bytes_sum": (int,),  # noqa: E501
            "iot_device_agg_sum": (int,),  # noqa: E501
            "iot_device_top99p_sum": (int,),  # noqa: E501
            "mobile_rum_session_count_android_sum": (int,),  # noqa: E501
            "mobile_rum_session_count_ios_sum": (int,),  # noqa: E501
            "mobile_rum_session_count_sum": (int,),  # noqa: E501
            "name": (str,),  # noqa: E501
            "netflow_indexed_events_count_sum": (int,),  # noqa: E501
            "npm_host_top99p": (int,),  # noqa: E501
            "opentelemetry_host_top99p": (int,),  # noqa: E501
            "profiling_host_top99p": (int,),  # noqa: E501
            "public_id": (str,),  # noqa: E501
            "rum_session_count_sum": (int,),  # noqa: E501
            "rum_total_session_count_sum": (int,),  # noqa: E501
            "synthetics_browser_check_calls_count_sum": (int,),  # noqa: E501
            "synthetics_check_calls_count_sum": (int,),  # noqa: E501
            "trace_search_indexed_events_count_sum": (int,),  # noqa: E501
            "twol_ingested_events_bytes_sum": (int,),  # noqa: E501
            "vsphere_host_top99p": (int,),  # noqa: E501
        }

    discriminator = None

    attribute_map = {
        "agent_host_top99p": "agent_host_top99p",  # noqa: E501
        "apm_azure_app_service_host_top99p": "apm_azure_app_service_host_top99p",  # noqa: E501
        "apm_host_top99p": "apm_host_top99p",  # noqa: E501
        "audit_logs_lines_indexed_sum": "audit_logs_lines_indexed_sum",  # noqa: E501
        "aws_host_top99p": "aws_host_top99p",  # noqa: E501
        "aws_lambda_func_count": "aws_lambda_func_count",  # noqa: E501
        "aws_lambda_invocations_sum": "aws_lambda_invocations_sum",  # noqa: E501
        "azure_app_service_top99p": "azure_app_service_top99p",  # noqa: E501
        "billable_ingested_bytes_sum": "billable_ingested_bytes_sum",  # noqa: E501
        "container_avg": "container_avg",  # noqa: E501
        "container_hwm": "container_hwm",  # noqa: E501
        "cspm_container_avg": "cspm_container_avg",  # noqa: E501
        "cspm_container_hwm": "cspm_container_hwm",  # noqa: E501
        "cspm_host_top99p": "cspm_host_top99p",  # noqa: E501
        "custom_ts_avg": "custom_ts_avg",  # noqa: E501
        "cws_container_count_avg": "cws_container_count_avg",  # noqa: E501
        "cws_host_top99p": "cws_host_top99p",  # noqa: E501
        "dbm_host_top99p_sum": "dbm_host_top99p_sum",  # noqa: E501
        "dbm_queries_avg_sum": "dbm_queries_avg_sum",  # noqa: E501
        "fargate_tasks_count_avg": "fargate_tasks_count_avg",  # noqa: E501
        "fargate_tasks_count_hwm": "fargate_tasks_count_hwm",  # noqa: E501
        "gcp_host_top99p": "gcp_host_top99p",  # noqa: E501
        "heroku_host_top99p": "heroku_host_top99p",  # noqa: E501
        "id": "id",  # noqa: E501
        "incident_management_monthly_active_users_hwm": "incident_management_monthly_active_users_hwm",  # noqa: E501
        "indexed_events_count_sum": "indexed_events_count_sum",  # noqa: E501
        "infra_host_top99p": "infra_host_top99p",  # noqa: E501
        "ingested_events_bytes_sum": "ingested_events_bytes_sum",  # noqa: E501
        "iot_device_agg_sum": "iot_device_agg_sum",  # noqa: E501
        "iot_device_top99p_sum": "iot_device_top99p_sum",  # noqa: E501
        "mobile_rum_session_count_android_sum": "mobile_rum_session_count_android_sum",  # noqa: E501
        "mobile_rum_session_count_ios_sum": "mobile_rum_session_count_ios_sum",  # noqa: E501
        "mobile_rum_session_count_sum": "mobile_rum_session_count_sum",  # noqa: E501
        "name": "name",  # noqa: E501
        "netflow_indexed_events_count_sum": "netflow_indexed_events_count_sum",  # noqa: E501
        "npm_host_top99p": "npm_host_top99p",  # noqa: E501
        "opentelemetry_host_top99p": "opentelemetry_host_top99p",  # noqa: E501
        "profiling_host_top99p": "profiling_host_top99p",  # noqa: E501
        "public_id": "public_id",  # noqa: E501
        "rum_session_count_sum": "rum_session_count_sum",  # noqa: E501
        "rum_total_session_count_sum": "rum_total_session_count_sum",  # noqa: E501
        "synthetics_browser_check_calls_count_sum": "synthetics_browser_check_calls_count_sum",  # noqa: E501
        "synthetics_check_calls_count_sum": "synthetics_check_calls_count_sum",  # noqa: E501
        "trace_search_indexed_events_count_sum": "trace_search_indexed_events_count_sum",  # noqa: E501
        "twol_ingested_events_bytes_sum": "twol_ingested_events_bytes_sum",  # noqa: E501
        "vsphere_host_top99p": "vsphere_host_top99p",  # noqa: E501
    }

    read_only_vars = {}

    _composed_schemas = {}

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """UsageSummaryDateOrg - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            agent_host_top99p (int): Shows the 99th percentile of all agent hosts over all hours in the current date for the given org.. [optional]  # noqa: E501
            apm_azure_app_service_host_top99p (int): Shows the 99th percentile of all Azure app services using APM over all hours in the current date for the given org.. [optional]  # noqa: E501
            apm_host_top99p (int): Shows the 99th percentile of all distinct APM hosts over all hours in the current date for the given org.. [optional]  # noqa: E501
            audit_logs_lines_indexed_sum (int): Shows the sum of all audit logs lines indexed over all hours in the current date for the given org.. [optional]  # noqa: E501
            aws_host_top99p (int): Shows the 99th percentile of all AWS hosts over all hours in the current date for the given org.. [optional]  # noqa: E501
            aws_lambda_func_count (int): Shows the sum of all AWS Lambda invocations over all hours in the current date for the given org.. [optional]  # noqa: E501
            aws_lambda_invocations_sum (int): Shows the sum of all AWS Lambda invocations over all hours in the current date for the given org.. [optional]  # noqa: E501
            azure_app_service_top99p (int): Shows the 99th percentile of all Azure app services over all hours in the current date for the given org.. [optional]  # noqa: E501
            billable_ingested_bytes_sum (int): Shows the sum of all log bytes ingested over all hours in the current date for the given org.. [optional]  # noqa: E501
            container_avg (int): Shows the average of all distinct containers over all hours in the current date for the given org.. [optional]  # noqa: E501
            container_hwm (int): Shows the high-water mark of all distinct containers over all hours in the current date for the given org.. [optional]  # noqa: E501
            cspm_container_avg (int): Shows the average number of Cloud Security Posture Management containers over all hours in the current date for the given org.. [optional]  # noqa: E501
            cspm_container_hwm (int): Shows the high-water mark of Cloud Security Posture Management containers over all hours in the current date for the given org.. [optional]  # noqa: E501
            cspm_host_top99p (int): Shows the 99th percentile of all Cloud Security Posture Management hosts over all hours in the current date for the given org.. [optional]  # noqa: E501
            custom_ts_avg (int): Shows the average number of distinct custom metrics over all hours in the current date for the given org.. [optional]  # noqa: E501
            cws_container_count_avg (int): Shows the average of all distinct Cloud Workload Security containers over all hours in the current date for the given org.. [optional]  # noqa: E501
            cws_host_top99p (int): Shows the 99th percentile of all Cloud Workload Security hosts over all hours in the current date for the given org.. [optional]  # noqa: E501
            dbm_host_top99p_sum (int): Shows the 99th percentile of all Database Monitoring hosts over all hours in the current month for all organizations.. [optional]  # noqa: E501
            dbm_queries_avg_sum (int): Shows the average of all distinct Database Monitoring normalized queries over all hours in the current month for all organizations.. [optional]  # noqa: E501
            fargate_tasks_count_avg (int): The average task count for Fargate.. [optional]  # noqa: E501
            fargate_tasks_count_hwm (int): Shows the high-water mark of all Fargate tasks over all hours in the current date for the given org.. [optional]  # noqa: E501
            gcp_host_top99p (int): Shows the 99th percentile of all GCP hosts over all hours in the current date for the given org.. [optional]  # noqa: E501
            heroku_host_top99p (int): Shows the 99th percentile of all Heroku dynos over all hours in the current date for the given org.. [optional]  # noqa: E501
            id (str): The organization id.. [optional]  # noqa: E501
            incident_management_monthly_active_users_hwm (int): Shows the high-water mark of incident management monthly active users over all hours in the current date for the given org.. [optional]  # noqa: E501
            indexed_events_count_sum (int): Shows the sum of all log events indexed over all hours in the current date for the given org.. [optional]  # noqa: E501
            infra_host_top99p (int): Shows the 99th percentile of all distinct infrastructure hosts over all hours in the current date for the given org.. [optional]  # noqa: E501
            ingested_events_bytes_sum (int): Shows the sum of all log bytes ingested over all hours in the current date for the given org.. [optional]  # noqa: E501
            iot_device_agg_sum (int): Shows the sum of all IoT devices over all hours in the current date for the given org.. [optional]  # noqa: E501
            iot_device_top99p_sum (int): Shows the 99th percentile of all IoT devices over all hours in the current date for the given org.. [optional]  # noqa: E501
            mobile_rum_session_count_android_sum (int): Shows the sum of all mobile RUM Sessions on Android over all hours in the current date for the given org.. [optional]  # noqa: E501
            mobile_rum_session_count_ios_sum (int): Shows the sum of all mobile RUM Sessions on iOS over all hours in the current date for the given org.. [optional]  # noqa: E501
            mobile_rum_session_count_sum (int): Shows the sum of all mobile RUM Sessions over all hours in the current date for the given org.. [optional]  # noqa: E501
            name (str): The organization name.. [optional]  # noqa: E501
            netflow_indexed_events_count_sum (int): Shows the sum of all Network flows indexed over all hours in the current date for the given org.. [optional]  # noqa: E501
            npm_host_top99p (int): Shows the 99th percentile of all distinct Networks hosts over all hours in the current date for the given org.. [optional]  # noqa: E501
            opentelemetry_host_top99p (int): Shows the 99th percentile of all hosts reported by the Datadog exporter for the OpenTelemetry Collector over all hours in the current date for the given org.. [optional]  # noqa: E501
            profiling_host_top99p (int): Shows the 99th percentile of all profiled hosts over all hours in the current date for the given org.. [optional]  # noqa: E501
            public_id (str): The organization public id.. [optional]  # noqa: E501
            rum_session_count_sum (int): Shows the sum of all browser RUM Sessions over all hours in the current date for the given org.. [optional]  # noqa: E501
            rum_total_session_count_sum (int): Shows the sum of RUM Sessions (browser and mobile) over all hours in the current date for the given org.. [optional]  # noqa: E501
            synthetics_browser_check_calls_count_sum (int): Shows the sum of all Synthetic browser tests over all hours in the current date for the given org.. [optional]  # noqa: E501
            synthetics_check_calls_count_sum (int): Shows the sum of all Synthetic API tests over all hours in the current date for the given org.. [optional]  # noqa: E501
            trace_search_indexed_events_count_sum (int): Shows the sum of all Indexed Spans indexed over all hours in the current date for the given org.. [optional]  # noqa: E501
            twol_ingested_events_bytes_sum (int): Shows the sum of all tracing without limits bytes ingested over all hours in the current date for the given org.. [optional]  # noqa: E501
            vsphere_host_top99p (int): Shows the 99th percentile of all vSphere hosts over all hours in the current date for the given org.. [optional]  # noqa: E501
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Helper creating a new instance from a response."""

        self = super(UsageSummaryDateOrg, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
