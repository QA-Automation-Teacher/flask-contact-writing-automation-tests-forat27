import time
import pytest
import uuid
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
    start = time.time()
    response = client.get(f"{BASE_URL}")
    end = time.time()
    assert end -start < 0.4, "GET response time is too slow"


def test_content_type_header_post(client):
    url = f"{BASE_URL}/contacts"
    response = client.post(url)
    assert "Content-Type" in response.headers


def test_create_contacts_post(client):
    new_contact={
        "name": "new name",
        "surname": "new surname",
        "email": "newfakeerrrrrr_email@gmail.com",
        "phone": "0501111111"
    }
    response = client.post(f"{BASE_URL}/api/contacts", json=new_contact)
    assert response.status_code in[200,201]
    response_data=response.get_json()
    assert (response_data["name"] == "new name" and
            response_data["surname"] == "new surname" and
            response_data["email"] == "newfakeerrrrrr_email@gmail.com" and
            response_data["phone"] == "0501111111"), "One or more fields do not match!"


def test_successful_delete_request(client):
    contact_id = 71
    delete_url = f"{BASE_URL}/api/contacts/{contact_id}"
    delete_response = client.delete(delete_url)
    assert delete_response.status_code in [200, 202, 204]
    get_response = client.get(delete_url)
    assert get_response.status_code == 404