from check_service_status import is_service_active

def test_localhost_is_active():

    print("\nEjecutando: test_local_is_active")
    assert is_service_active("localhost") == True, "¡Localhost debería estar activo!" 

def test_unknown_host_is_inactive():

    hostname_inventado = 'hostinventado123xyz.com'
    assert is_service_active(hostname_inventado) == False, f"{hostname_inventado} no debería estar activo"

def test_another_active_host():
    assert is_service_active("awakelab.cl") == True, "google.com debería estar activo!"

