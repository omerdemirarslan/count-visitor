import json
import os
import requests
import unittest


class VisitorCounterServiceTestCase(unittest.TestCase):
    api_url = "http://0.0.0.0:8080"
    visitor_count_enpoint = "/api/v1/visitor/count"
    dir_path = os.path.dirname(os.path.abspath(__file__))

    def test_get_service_status(self):
        url = "%s%s" % (self.api_url, self.visitor_count_enpoint)

        with open(os.path.join(self.dir_path, 'json_data/visitor_count_data.json')) as file:
            json_data = file.read()

        response = requests.post(
            url=url,
            json=json_data
        )

        self.assertEqual(response.status_code, 200)

    def test_calculated_visitor_count_data(self):
        url = "%s%s" % (self.api_url, self.visitor_count_enpoint)

        with open(os.path.join(self.dir_path, 'json_data/visitor_count_data.json')) as file:
            json_data = file.read()

        response = requests.post(
            url=url,
            json=json.loads(json_data)
        )

        json_data = json.loads(response.text)

        self.assertTrue(json_data["data"])


if __name__ == '__main__':
    unittest.main()
