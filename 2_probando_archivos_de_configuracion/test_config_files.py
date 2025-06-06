import os
import pytest

def test_main_config_file_exists():
    config_path = r"C:\tmp_test_files\my_app_port.conf"

    assert os.path.exists(config_path), f"El archivo de configuración {config_path} no fue encontrado."

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

def test_port_configuration_is_created():
    config_path = r"C:\tmp_test_files"
    config_filename = "my_app_port.conf"
    config_file_test = os.path.join(config_path, config_filename)

    expected_port = "8080"
    key_to_check = "PORT"

    if not os.path.exists(config_path):
        try:
            os.makedirs(config_path)
        except OSError as e:
            pytest.fail(f"No se pudo crear el directorio {config_path}: {e}")
    
    try:
        with open(config_file_test, "w") as f:
            f.write(f"{key_to_check}={expected_port}\n")
            f.write("ANOTHER_KEY=some_value")
    except OSError as e:
        pytest.fail(f"No se pudo escribir en el archivo {config_file_test}: {e}")


    port = get_value_from_config_file(config_file_test, key_to_check)
    assert port == expected_port, f"Se esperaba el puerto {expected_port}, pero se obtuvo {port} en {config_file_test}"
