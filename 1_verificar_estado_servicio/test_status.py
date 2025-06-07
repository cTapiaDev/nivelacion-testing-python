from check_service_status import is_service_active # Importamos la función que vamos a probar

def test_localhost_is_active():
    """
    Probamos si localhost responde o no al ping.
    Debería responder siempre.
    """
    print("\nEjecutando: test_local_is_active")
    assert is_service_active("localhost") == True, "¡Localhost debería estar activo!" 
    # La palabra assert es clave. Significa "afirmo que la condición es Verdadera"
    # En caso de no cumplirse assert, la prueba falla.


def test_unknown_host_is_inactive():
    """
    Va a probar si efectivamente falla un host que no existe.
    """
    hostname_inventado = 'hostinventado123xyz.com'
    assert is_service_active(hostname_inventado) == False, f"{hostname_inventado} no debería estar activo"

def test_another_active_host():
    """
    Prueba directa sobre un host público al que debería existir acceso.
    """
    assert is_service_active("awakelab.cl") == True, "google.com debería estar activo!"


# Resumen:
"""
Creamos una herramienta simple (is_service_active) que un DevOps usaría. También añadimos las pruebas directas para ver si funcionan.
Si modifican is_service_active y se rompe, las pruebas nos avisarán inmediatamente. Esta es la base de la confianza en la automatización.
"""

