"""
Update an SLO correction returns "OK" response using JSON:API models
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.service_level_objective_corrections_api import ServiceLevelObjectiveCorrectionsApi
from datadog_api_client.v1.model.slo_correction_category import SLOCorrectionCategory
from datadog_api_client.v1.model.slo_correction_update_request import SLOCorrectionUpdateRequestJSON

# there is a valid "correction" for "slo"
CORRECTION_DATA_ID = environ["CORRECTION_DATA_ID"]

body = SLOCorrectionUpdateRequestJSON(
    category=SLOCorrectionCategory.DEPLOYMENT,
    description="Example-Service-Level-Objective-Correction",
    end=int((datetime.now() + relativedelta(hours=1)).timestamp()),
    start=int(datetime.now().timestamp()),
    timezone="UTC",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ServiceLevelObjectiveCorrectionsApi(api_client)
    response = api_instance.update_slo_correction(slo_correction_id=CORRECTION_DATA_ID, body=body)

    print(response)
