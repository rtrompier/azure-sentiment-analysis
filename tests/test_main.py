import unittest
import json
import azure.functions as func

from sentiment_analysis.main import entry_point

class TestSentimentAnalysis(unittest.TestCase):
    def test_valid_response(self):
        # Construct a mock Queue message.
        req = func.HttpRequest(
            method='GET', 
            body=None,
            url='/sentiment_analysis',
            params={'sentence': 'Hello'}
        )

        # # Call the function.
        response = entry_point(req)

        # # Check the output.
        body = json.loads(response.get_body())
        self.assertTrue(isinstance(body, list))

        result = body[0]
        self.assertTrue(result.keys(), ['label', 'score'])



    def test_error_response(self):
        # Construct a mock Queue message.
        req = func.HttpRequest(
            method='GET', 
            body=None,
            url='/sentiment_analysis'
        )

        # # Call the function.
        response = entry_point(req)

        # # Check the output.
        body = json.loads(response.get_body())
        self.assertTrue(body.keys(), ['error'])