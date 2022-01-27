from unittest import TestCase

from fastapi.testclient import TestClient

from trader_api.main import app

client = TestClient(app)


class TestInternal(TestCase):

    def test_ping(self):
        """Tests /_internal/ping endpoint."""

        response = client.get('/_internal/ping')
        self.assertEqual(
            response.status_code, 200,
            'Incorrect ping status code.'
        )
        self.assertEqual(
            response.json(), {'result': 'pong'},
            'Ping endpoint returns incorrect body.'
        )
