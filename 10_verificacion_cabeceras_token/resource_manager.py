import os
import requests

def get_protected_resources():
    """
    Obtiene una lista de recursos de un Endpoint protegido.
    Requiere que la variable de entorno 'API_AUTH_TOKEN' esté configurada.
    """

    # os.environ.get() es la forma segura. Si la variable no existe, devuelve None.
    api_token = os.environ.get("API_AUTH_TOKEN")

    # Es crucial manejar el token en caso de que no esté configurado.
    if not api_token:
        print("[ERROR] la variable de entorno no está configurada.")
        raise ValueError("El token de API es obligatorio")
    
    headers = {
        "Authorization": f"Bearer {api_token}"
    }

    url = "https://api.example.com/v1/resources"

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Falló la petición a la API: {e}")
        return None

