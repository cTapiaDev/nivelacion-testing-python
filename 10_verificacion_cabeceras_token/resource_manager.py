import os
import requests

def get_protected_resources():

    api_token = os.environ.get("API_AUTH_TOKEN")

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

