import pytest
import os
import tempfile

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

@pytest.fixture
def temp_config_file_with_port():
    tf = tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".conf")
    config_content = "HOST=127.0.0.1 \n PORT=9999 \n USER=test_user"
    tf.write(config_content)
    tf_path = tf.name
    tf.close()

    yield tf_path

    os.remove(tf_path)

def test_read_port_from_fixture_config(temp_config_file_with_port):

    filepath = temp_config_file_with_port
    expected_port = "9999"
    key_to_check = "PORT"

    port = get_value_from_config_file(filepath, key_to_check)
    assert port == expected_port, f"Se esperaba el puerto {expected_port} pero se obtuvo {port} desde la fixture config."

def test_read_host_from_fixture_config(temp_config_file_with_port):
    
    filepath = temp_config_file_with_port
    expected_host = "127.0.0.1"
    key_to_check = "HOST"

    host = get_value_from_config_file(filepath, key_to_check)
    assert host == expected_host, f"Se esperaba el host {expected_host} pero se obtuvo {host} desde la fixture config"