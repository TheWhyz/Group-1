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

    def test_create_counter(self, client):
        """It should create a counter"""
        result = client.post('/counters/foo')
        assert result.status_code == status.HTTP_201_CREATED
    
    # Student 1: 
    def test_create_new_counter(self, client):
        """It should create a counter"""
        result = client.post('/counters/foooo')
        assert result.status_code == status.HTTP_201_CREATED
        
    # Student 2: BRENDA CORONADO    
    def test_duplicate_counter(self, client):
        """It should create a counter and prevent duplicates"""
        # First request should succeed
        result = client.post('/counters/fooo')
        assert result.status_code == status.HTTP_201_CREATED

        # Second request with the same name should fail
        duplicate_result = client.post('/counters/fooo')
        assert duplicate_result.status_code == status.HTTP_409_CONFLICT
        assert duplicate_result.get_json() == {"error": "Counter fooo already exists"}

    # Student 3: Joseph Dib
    def test_get_counter(self, client):
            """It should get a counter"""
            result = client.post('/counters/foo')
            result = client.get('/counters/foo')
            assert result.status_code == status.HTTP_201_CREATED
    
    # Student 4
    def test_get_non_existent_counter(self, client):
        """It should return 404 for a non-existent counter"""
        result = client.get('/counters/nonexistent')
        assert result.status_code == status.HTTP_404_NOT_FOUND

    # Evan Hollingshead - 5
    def test_increment_counter(self, client):
        """Should increment a counter"""
        counter_name = "test_counter"
        client.post(f"/counters/{counter_name}")
        response = client.put(f"/counters/{counter_name}")
        assert response.status_code == status.HTTP_200_OK
        assert response.get_json() == {counter_name: 1}
        response = client.put(f"/counters/{counter_name}")
        assert response.get_json() == {counter_name: 2}

    # Student 6 Rubi Escobedo
    def test_increment_non_existent_counter(self, client):
        """It should not increment a non-existent counter"""
        response = client.put("/counters/does_not_exist")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.get_json() == {"error": "Counter does_not_exist not found"}

    # Student 7
    def test_delete_counter(self, client):
        """It should delete an existing counter"""
        client.post('/counters/my_counter')
        response = client.delete('/counters/my_counter')
        assert response.status_code == status.HTTP_200_OK
        
    # Student 8
    def test_delete_nonexistent_counter(self, client):
        """It should not delete a non-existent counter"""
        result = client.delete('/counters/nonexistent')
        assert result.status_code == status.HTTP_404_NOT_FOUND
        