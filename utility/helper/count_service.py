""" Counter Service Base Helper File """
from .constant_variables import READABLE_DATA


class VisitorCountService:
    """ Visitor Count Service For All Visitors Processes """

    @staticmethod
    def calculate_visitor_entry_and_exit(hour_interval: str, entry_exit_data: dict, current_visitor: int) -> dict:
        """
        This Method Calculates Hourly Distribution Entry and Exit Data
        :param hour_interval:
        :param entry_exit_data:
        :param current_visitor:
        :return:
        """
        hourly_entry_data = 0
        hourly_exit_data = 0

        for item in entry_exit_data:
            if item["type"] == "in":
                hourly_entry_data += item["value"]
            if item["type"] == "out":
                hourly_exit_data += item["value"]

        hourly_inside_data = hourly_entry_data - hourly_exit_data + current_visitor

        calculated_data = {
            "hour_interval": hour_interval,
            "hourly_entry_data": hourly_entry_data,
            "hourly_exit_data": hourly_exit_data,
            "hourly_inside_data": hourly_inside_data
        }

        return calculated_data

    def get_hour_interval_and_entry_exit_data(self, visitors_data: dict) -> dict:
        """
        This Method Gets Hour Interval and Visitor Entry/Exit Data By Visitors Data
        :param visitors_data:
        :return:
        """
        calculated_data = {"hourly_inside_data": 0}
        result = []

        for hour_interval, entry_exit_data in visitors_data.items():
            calculated_data = self.calculate_visitor_entry_and_exit(
                hour_interval=hour_interval,
                entry_exit_data=entry_exit_data,
                current_visitor=calculated_data["hourly_inside_data"]
            )

            result.append(calculated_data)

        return self.convert_calculated_visitor_data_to_readable_data(calculate_data=result)

    @staticmethod
    def convert_calculated_visitor_data_to_readable_data(calculate_data: list) -> dict:
        """
        This Method Returns Readable Calculated Visitor Count Data
        :param calculate_data:
        :return:
        """
        result = {"data": []}

        for data in calculate_data:
            result["data"].append(
                READABLE_DATA.format(
                    hour_interval=data["hour_interval"],
                    entry_count=data["hourly_entry_data"],
                    exit_count=data["hourly_exit_data"],
                    current_count=data["hourly_inside_data"]

                )
            )

        return result
