import pytest
import os
from resource_manager import get_protected_resources

def test_get_protected_resources_correct(mocker):
    """
    Verifica que el script lee un token de una variable de entorno (simulada).
    Lo formatea correctamente y lo envía a la cabecera Authorization.
    """
    mock_get = mocker.patch('resource_manager.requests.get')
    # Configuramos una respuesta de éxito genérica.
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"id": "res-123", "name": "Servidor de Base de Datos"}]

    # Mock para la variable de entorno.
    fake_token = "un-token-secreto-y-seguro-para-la-prueba"
    # mocker.patch.dict simula que os.environ tiene esta clave y valor solo para la prueba.
    mocker.patch.dict(os.environ, {"API_AUTH_TOKEN": fake_token})
    print(f"Variable de entorno: 'API_AUTH_TOKEN' simulada")

    get_protected_resources()

    mock_get.assert_called_once()
    call_arguments = mock_get.call_args
    sent_headers = call_arguments.kwargs['headers']
    print(f"Cabeceras dentro del mock: {sent_headers}")

    # Verificamos que la cabecera Authorization existe, además de que tiene el formato y token correctos.
    assert "Authorization" in sent_headers
    assert sent_headers["Authorization"] == f"Bearer {fake_token}"
    print("¡La autenticación es correcta!")

def test_get_protected_resources_error_missing(mocker):
    """
    Verifica que la función lanza un ValueError si la variable de entorno NO está configurada.
    """

    # Usamos patch.dict para establecer un entorno vacío o sin clave.
    mocker.patch.dict(os.environ, clear=True) # 'clear=True' simula un entorno sin variables.

    # Pytest tiene una forma de verificar que se lanza una excepción específica.
    with pytest.raises(ValueError) as excinfo:
        get_protected_resources()

    # Aquí verificamos el mensaje de la excepción.
    assert "El token de API es obligatorio" in str(excinfo.value)
    print("La función lanzó un ValueError como se espera cuando no tenemos la variable de entorno")