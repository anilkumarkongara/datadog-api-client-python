"""
Create an SLO correction returns "OK" response using JSON:API models
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
from datadog_api_client.v1.model.slo_correction_create_request import SLOCorrectionCreateRequestJSON

# there is a valid "slo" in the system
SLO_DATA_0_ID = environ["SLO_DATA_0_ID"]

body = SLOCorrectionCreateRequestJSON(
    category=SLOCorrectionCategory.SCHEDULED_MAINTENANCE,
    description="Example-Service-Level-Objective-Correction",
    end=int((datetime.now() + relativedelta(hours=1)).timestamp()),
    slo_id=SLO_DATA_0_ID,
    start=int(datetime.now().timestamp()),
    timezone="UTC",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    response = api_instance.create_slo_correction(body=body)

    print(response)
