"""
Test Cases for Counter Web Service

Create a service that can keep a track of multiple counters
- API must be RESTful - see the status.py file. Following these guidelines, you can make assumptions about
how to call the web service and assert what it should return.
- The endpoint should be called /counters
- When creating a counter, you must specify the name in the path.
- Duplicate names must return a conflict error code.
- The service must be able to update a counter by name.
- The service must be able to read the counter
"""
import pytest
from src import app
from src import status

@pytest.fixture()
def client():
    """Fixture for Flask test client"""
    return app.test_client()

@pytest.mark.usefixtures("client")
class TestCounterEndpoints:
    """Test cases for Counter API"""

    def test_reset_all_counters(self, client):
        """It should reset all counters"""
        # Create a counter
        client.post('/counters/foo')
        client.put('/counters/foo', json={"value": 10})

        # Reset all counters
        result = client.post('/counters/reset')

        assert result.status_code == status.HTTP_200_OK
        assert result.get_json() == {"message": "All counters reset"}
