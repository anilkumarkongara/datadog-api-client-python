# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.incident_todo_assignee_array import IncidentTodoAssigneeArray
from datadog_api_client.v2.model.incident_todo_assignee_array import IncidentTodoAssigneeArray

if TYPE_CHECKING:
    from datadog_api_client.v2.model.incident_todo_patch_data import IncidentTodoPatchData


@dataclass
class IncidentTodoPatchRequestJSON:
    assignees: Union[IncidentTodoAssigneeArray, UnsetType] = unset
    completed: Union[str, none_type, UnsetType] = unset
    content: Union[str, UnsetType] = unset
    due_date: Union[str, none_type, UnsetType] = unset
    incident_id: Union[str, UnsetType] = unset


class IncidentTodoPatchRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.incident_todo_patch_data import IncidentTodoPatchData

        return {
            "data": (IncidentTodoPatchData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = IncidentTodoPatchRequestJSON

    def __init__(self_, data: IncidentTodoPatchData, **kwargs):
        """
        Patch request for an incident todo.

        :param data: Incident todo data for a patch request.
        :type data: IncidentTodoPatchData
        """
        super().__init__(kwargs)

        self_.data = data
