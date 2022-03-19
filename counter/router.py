from counter import app, Request, status

from utility.helper.count_service import VisitorCountService


@app.post("/api/v1/visitor/count", tags=["Visitor Count"])
async def visitor_count(request: Request):
    """
    This Method Handle Visitor Count Requests
    :param request:
    :return:
    """
    visitor_converted_data = await request.json()

    if isinstance(visitor_converted_data, dict):
        visitor_count_servise = VisitorCountService()

        visitor_entry_exit_data = visitor_count_servise.get_hour_interval_and_entry_exit_data(
            visitors_data=visitor_converted_data
        )

        return visitor_entry_exit_data
    else:
        response = {
                "data": [],
                "status": status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                "message": "Sent Data Type Must Be JSON"
            }

        return response
