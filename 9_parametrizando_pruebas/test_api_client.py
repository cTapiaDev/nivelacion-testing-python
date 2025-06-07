import pytest
import requests # Importamos request para importar sus clases de excepción
from api_client import get_user_data

# --- Test para cuando la API responde correctamente ---
def test_get_user_data_success(mocker):
    """
    Prueba que get_user_data procesa correctamente una respuesta exitosa de la API
    """

    # mocker.patch() es nuestro simulador. Le decimos qué reemplazar.
    # api_client.requests.get -> significa "la función get del módulo requests"
    mock_get = mocker.patch('api_client.requests.get')

    # Datos falsos que nuestra API simulada devuelve
    fake_api_response = {
        "id": 1,
        "name": "Leanne Graham",
        "email": "Sincere@april.biz"
    }

    # mock_get retorna un objeto falso que se comporta como una respuesta requests
    mock_get.return_value.status_code = 200
    # mock_get que su método .json() debe retornar nuestros datos falsos
    mock_get.return_value.json.return_value = fake_api_response

    user_id_to_test = 1
    user_data = get_user_data(user_id_to_test)

    # Verificamos que se llamó a nuestro mock una vez y con la URL correcta
    mock_get.assert_called_once_with(f"https://jsonplaceholder.typicode.com/users/{user_id_to_test}", timeout=5)
    # Verificamos que nuestra función devolvió los datos que el mock le dio
    assert user_data is not None
    assert user_data["name"] == "Leanne Graham"
    assert user_data["email"] == "Sincere@april.biz"
    print("Prueba completada con éxito.")

def test_get_user_data_not_found(mocker):
    """
    Prueba que get_user_data maneja correctamente un error 404.
    """
    mock_get = mocker.patch('api_client.requests.get')

    # En este test la llamada a .raise_for_status() queremos que lance un error.
    # con 'side_effect' para decirle a un mock que, cuando lo llamen, ejecuta una acción.
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error: Not Found for url")

    user_data = get_user_data(999)

    # Verificamos que se llamó al mock.
    mock_get.assert_called_once()
    # Verificamos que nuestra función manejó la excepción y devolvió None.
    assert user_data is None
    print("Prueba de error 404 completa.")


@pytest.mark.parametrize(
        # Un string con los nombres de los parámetros para la prueba
        "error_a_simular",
        # Una lista de tuplas. Cada tupla es un set de valores para los parámetros.
        [
            (requests.exceptions.ConnectionError("Fallo de conexión simulado")),
            (requests.exceptions.Timeout("Timeout simulado")),
            (requests.exceptions.HTTPError("Server error: service unavailable"))
        ]
)
def test_get_user_data_networks_error(mocker, error_a_simular):
    """
    Esta única función de prueba verifica múltiples escenarios de error de red
    """
    mock_get = mocker.patch('api_client.requests.get')

    # Configuramos el mock para que, cuando lo llamen, directamente lance la excepción que nos viene del parámetro.
    mock_get.side_effect = error_a_simular

    result = get_user_data(5)

    # La aserción es la misma para todos los casos de error: esperamos que devuelva None.
    assert result is None
    print("Prueba de error parametrizada al completo.")

