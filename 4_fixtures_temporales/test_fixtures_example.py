import pytest
import os
import tempfile # Este módulo nos permite crear archivos y directorios temporales.

def get_value_from_config_file(filepath, key_to_find):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            if key.strip() == key_to_find:
                return value.strip()
    return None

@pytest.fixture # Decorador que indica que esto es una fixture.
def temp_config_file_with_port():
    """
    La fixture crea un archivo temporal con un puerto definido.
    Proporciona la ruta a este archivo de prueba.
    Y al final limpia el archivo temporal.
    """
    tf = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".conf")
    # tempfile.NamedTemporaryFile crea un archivo que se borra cuando se cierra.
    # delete=False es importante aquí porque queremos que el archivo exista mientras la prueba lo usa. Luego del yield lo eliminamos manualmente.
    config_content = "HOST=127.0.0.1 \n PORT=9999 \n USER=test_user"
    tf.write(config_content)
    tf_path = tf.name # Aquí guardamos la ruta del archivo temporal
    tf.close() # Cerramos el archivo para que la prueba pueda abrirlo

    yield tf_path # Aquí la fixture entrega el valor a la prueba. Ahora es cuando se ejecuta.

    os.remove(tf_path) # Borramos el archivo manualmente.


# --- Estas pruebas usan la fixture ---
def test_read_port_from_fixture_config(temp_config_file_with_port):
    """
    Aquí vamos a recibir el archivo temporal de la fixture.
    """
    filepath = temp_config_file_with_port
    expected_port = "9999"
    key_to_check = "PORT"

    port = get_value_from_config_file(filepath, key_to_check)
    assert port == expected_port, f"Se esperaba el puerto {expected_port} pero se obtuvo {port} desde la fixture config."

def test_read_host_from_fixture_config(temp_config_file_with_port):
    """
    Aquí usamos la misma fixture
    """
    filepath = temp_config_file_with_port
    expected_host = "127.0.0.1"
    key_to_check = "HOST"

    host = get_value_from_config_file(filepath, key_to_check)
    assert host == expected_host, f"Se esperaba el host {expected_host} pero se obtuvo {host} desde la fixture config"


"""
Las fixtures nos van a permitir separar la preparación del entorno de prueba.
En DevOps esto es oro puro, porque podemos tener fixtures que preparen contenedores docker,
simulen servicios de red o creen estructuras de directorios complejas, etc.
Así, nuestras pruebas las usan sin preocuparse por los detalles de su creación o destrucción.
"""