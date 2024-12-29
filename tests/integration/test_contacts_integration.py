import time
BASE_URL = "http://localhost:5000"

def setup_module(module):
    pass


def teardown_module(module):
    pass


def test_get_contacts(client):
    response = client.get(BASE_URL + "/api/contacts")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_response_time_get2(client):
    user_id=1
    start = time.time()
    response = client.get(f"{BASE_URL}/{user_id}")
    end = time.time()
    assert end -start < 0.4, "GET response time is too slow"