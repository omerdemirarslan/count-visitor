import logging

from counter import app, Request, status, responses
from utility.helper.count_service import VisitorCountService

logger = logging.getLogger(__name__)


@app.post("/api/v1/visitor/count", tags=["Visitor Count"])
async def visitor_count(request: Request):
    """
    This Method Handle Visitor Count Requests
    :param request:
    :return:
    """
    try:
        visitor_converted_data = await request.json()
    except Exception as err:
        logger.error(err)

        return responses.JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": "Sent Data Type Must Be JSON"
            }

        )

    if isinstance(visitor_converted_data, dict):
        visitor_count_service = VisitorCountService()

        visitor_entry_exit_data = visitor_count_service.get_hour_interval_and_entry_exit_data(
            visitors_data=visitor_converted_data
        )

        return visitor_entry_exit_data
    else:
        return responses.JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": "Sent Data Type Must Be JSON"
            }
        )
