from counter import app, Request

from utility.helper.count_service import VisitorCountService


@app.post("/api/v1/visitor/count", tags=["Visitor Count"])
async def visitor_count(visitor_data: Request):
    """
    This Method Handle Visitor Count Requests
    :param visitor_data:
    :return:
    """
    visitor_converted_data = await visitor_data.json()

    visitor_count_servise = VisitorCountService()

    visitor_entry_exit_data = visitor_count_servise.calculate_visitor_entry_and_exit(
        entry_exit_data=visitor_converted_data
    )

    return visitor_entry_exit_data
