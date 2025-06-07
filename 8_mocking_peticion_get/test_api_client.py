import pytest
import requests
from api_client import get_user_data


def test_get_user_data_success(mocker):
    
    mock_get = mocker.patch('api_client.requests.get')

    fake_api_response = {
        "id": 1,
        "name": "Leanne Graham",
        "email": "Sincere@april.biz"
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = fake_api_response

    user_id_to_test = 1
    user_data = get_user_data(user_id_to_test)

    mock_get.assert_called_once_with(f"https://jsonplaceholder.typicode.com/users/{user_id_to_test}", timeout=5)

    assert user_data is not None
    assert user_data["name"] == "Leanne Graham"
    assert user_data["email"] == "Sincere@april.biz"
    print("Prueba completada con éxito.")

def test_get_user_data_not_found(mocker):

    mock_get = mocker.patch('api_client.requests.get')

    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error: Not Found for url")

    user_data = get_user_data(999)

    mock_get.assert_called_once()
    assert user_data is None
    print("Prueba de error 404 completa.")

