import requests

# Definimos la URL base de la API
API_BASE_URL = "https://jsonplaceholder.typicode.com"

def get_user_data(user_id):
    """
    Obtendremos los datos de un usuario específico de la API JSONPlaceholder
    """
    url = f"{API_BASE_URL}/users/{user_id}" # URL completa

    # Es importante el uso de try - except, no sabemos cuando la red puede fallar o el servidor estar caído.
    try:
        # Hacemos la petición GET.
        # Con el timeout=5 si el servidor no responde en 5 segundos, la petición fallará en lugar de dejar el proceso colgado.
        response = requests.get(url, timeout=5)

        # Si la respuesta fue un error, raise_for_status lanzará una excepción que será capturada por el bloque except.
        response.raise_for_status()

        # Con todo correcto, la API nos devuelve datos en formato JSON
        # .json() convierte la respuesta en un diccionario de Python.
        print(f"[CLIENTE] Respuesta recibida con código {response.status_code}...")
        return response.json()
    

    # Capturamos errores específicos para personalizar mejor los mensajes.
    except requests.exceptions.HTTPError as err:
        # Este se activa si raise_for_status genera un error.
        print(f"[ERROR] Error HTTP: {err}")
        return None
    
    except requests.exceptions.ConnectionError as err:
        # Esto ocurre si no podemos conectar con el servidor.
        print(f"[ERROR] Error de conexión: {err}")
        return None
    
    except requests.exceptions.Timeout as err:
        # Si tarda más de 5 segundos en responder.
        print(f"[ERROR] La petición de timeout tardó más de 5 segundos: {err}")
        return None
    
    except requests.exceptions.RequestException as err:
        # 'catch-all' para capturar cualquier otro error que pueda gestionar la librería requests.
        print(f"[ERROR] Hubo un error inesperado: {err}")
        return None
    
# if __name__ == "__main__":
#     user = get_user_data(1)
#     if user:
#         print(f"Datos del usuario 1 - Nombre: {user.get('name')}, Email: {user.get('email')}")
    
    
#     user_not_found = get_user_data(98)
#     if user_not_found is None:
#         print(f"El script nos demuestra que el usuario efectivamente no existe")