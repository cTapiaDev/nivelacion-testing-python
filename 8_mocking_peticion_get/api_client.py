import requests

API_BASE_URL = "https://jsonplaceholder.typicode.com"

def get_user_data(user_id):

    url = f"{API_BASE_URL}/users/{user_id}"

    try:
        response = requests.get(url, timeout=5)

        response.raise_for_status()

        print(f"[CLIENTE] Respuesta recibida con código {response.status_code}...")
        return response.json()
    
    except requests.exceptions.HTTPError as err:
        print(f"[ERROR] Error HTTP: {err}")
        return None
    
    except requests.exceptions.ConnectionError as err:
        print(f"[ERROR] Error de conexión: {err}")
        return None
    
    except requests.exceptions.Timeout as err:
        print(f"[ERROR] La petición de timeout tardó más de 5 segundos: {err}")
        return None
    
    except requests.exceptions.RequestException as err:
        print(f"[ERROR] Hubo un error inesperado: {err}")
        return None
    
# if __name__ == "__main__":
#     user = get_user_data(1)
#     if user:
#         print(f"Datos del usuario 1 - Nombre: {user.get('name')}, Email: {user.get('email')}")
    
    
#     user_not_found = get_user_data(98)
#     if user_not_found is None:
#         print(f"El script nos demuestra que el usuario efectivamente no existe")