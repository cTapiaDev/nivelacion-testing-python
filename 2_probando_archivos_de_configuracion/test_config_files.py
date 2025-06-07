import os
import pytest

# --- Verificar existencia de un archivo ---
def test_main_config_file_exists():
    """
    Verifica si un archivo importante existe.
    Para este ejemplo, creamos el archivo manualmente antes de ejecutar pytest.
    Si el archivo no existe, la prueba falla.
    """
    config_path = r"C:\tmp_test_files\my_app_port.conf"

    assert os.path.exists(config_path), f"El archivo de configuración {config_path} no fue encontrado."



# Función que nos ayuda a leer un valor de un archivo 'clave=valor'
def get_value_from_config_file(filepath, key_to_find):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip() # Limpia espacios y saltos de línea
            if line.startswith("#") or "=" not in line: # Ignora líneas sin '='
                continue
            key, value = line.split("=", 1) # Divide solo en el primer '=' que encuentra
            if key.strip() == key_to_find:
                return value.strip()
    
    return None


# --- Verificar contenido de un archivo ---
def test_port_configuration_is_created():

    # Definimos el directorio y el nombre del archivo
    config_path = r"C:\tmp_test_files"
    config_filename = "my_app_port.conf"
    config_file_test = os.path.join(config_path, config_filename)

    expected_port = "8080"
    key_to_check = "PORT"


    # Esto no es un directorio temporal gestionado por pytest, por eso nos debemos asegurar de que existe antes de intentar escribir en el archivo.
    if not os.path.exists(config_path):
        try:
            os.makedirs(config_path)
        except OSError as e:
            # Si no podemos crear el directorio, el test debe terminar aquí.
            pytest.fail(f"No se pudo crear el directorio {config_path}: {e}")
    

    # Creamos el archivo con contenido para la prueba
    try:
        with open(config_file_test, "w") as f:
            f.write(f"{key_to_check}={expected_port}\n")
            f.write("ANOTHER_KEY=some_value")
    except OSError as e:
        pytest.fail(f"No se pudo escribir en el archivo {config_file_test}: {e}")


    # Aquí verificamos el contenido (Esto es lo que realmente le interesa al test)
    port = get_value_from_config_file(config_file_test, key_to_check)
    assert port == expected_port, f"Se esperaba el puerto {expected_port}, pero se obtuvo {port} en {config_file_test}"

    # En caso de que quisieran borrar el archivo luego de la prueba, pueden usar el siguiente código ->
    # if os.path.exists(config_file_test):
    #     os.remove(config_file_test)
