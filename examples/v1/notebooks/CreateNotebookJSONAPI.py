"""
Create a notebook returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.notebooks_api import NotebooksApi
from datadog_api_client.v1.model.notebook_cell_create_request import NotebookCellCreateRequest
from datadog_api_client.v1.model.notebook_cell_resource_type import NotebookCellResourceType
from datadog_api_client.v1.model.notebook_create_request import NotebookCreateRequestJSON
from datadog_api_client.v1.model.notebook_graph_size import NotebookGraphSize
from datadog_api_client.v1.model.notebook_markdown_cell_attributes import NotebookMarkdownCellAttributes
from datadog_api_client.v1.model.notebook_markdown_cell_definition import NotebookMarkdownCellDefinition
from datadog_api_client.v1.model.notebook_markdown_cell_definition_type import NotebookMarkdownCellDefinitionType
from datadog_api_client.v1.model.notebook_relative_time import NotebookRelativeTime
from datadog_api_client.v1.model.notebook_split_by import NotebookSplitBy
from datadog_api_client.v1.model.notebook_status import NotebookStatus
from datadog_api_client.v1.model.notebook_timeseries_cell_attributes import NotebookTimeseriesCellAttributes
from datadog_api_client.v1.model.timeseries_widget_definition import TimeseriesWidgetDefinition
from datadog_api_client.v1.model.timeseries_widget_definition_type import TimeseriesWidgetDefinitionType
from datadog_api_client.v1.model.timeseries_widget_request import TimeseriesWidgetRequest
from datadog_api_client.v1.model.widget_axis import WidgetAxis
from datadog_api_client.v1.model.widget_display_type import WidgetDisplayType
from datadog_api_client.v1.model.widget_line_type import WidgetLineType
from datadog_api_client.v1.model.widget_line_width import WidgetLineWidth
from datadog_api_client.v1.model.widget_live_span import WidgetLiveSpan
from datadog_api_client.v1.model.widget_request_style import WidgetRequestStyle

body = NotebookCreateRequestJSON(
    cells=[
        NotebookCellCreateRequest(
            attributes=NotebookMarkdownCellAttributes(
                definition=NotebookMarkdownCellDefinition(
                    text="## Some test markdown\n\n```js\nvar x, y;\nx = 5;\ny = 6;\n```",
                    type=NotebookMarkdownCellDefinitionType.MARKDOWN,
                ),
            ),
            type=NotebookCellResourceType.NOTEBOOK_CELLS,
        ),
        NotebookCellCreateRequest(
            attributes=NotebookTimeseriesCellAttributes(
                definition=TimeseriesWidgetDefinition(
                    requests=[
                        TimeseriesWidgetRequest(
                            display_type=WidgetDisplayType.LINE,
                            q="avg:system.load.1{*}",
                            style=WidgetRequestStyle(
                                line_type=WidgetLineType.SOLID,
                                line_width=WidgetLineWidth.NORMAL,
                                palette="dog_classic",
                            ),
                        ),
                    ],
                    show_legend=True,
                    type=TimeseriesWidgetDefinitionType.TIMESERIES,
                    yaxis=WidgetAxis(
                        scale="linear",
                    ),
                ),
                graph_size=NotebookGraphSize.MEDIUM,
                split_by=NotebookSplitBy(
                    keys=[],
                    tags=[],
                ),
                time=None,
            ),
            type=NotebookCellResourceType.NOTEBOOK_CELLS,
        ),
    ],
    name="Example-Notebook",
    status=NotebookStatus.PUBLISHED,
    time=NotebookRelativeTime(
        live_span=WidgetLiveSpan.PAST_ONE_HOUR,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = NotebooksApi(api_client)
    response = api_instance.create_notebook(body=body)

    print(response)
