import os # os = operating system

def is_service_active(hostname):
# def is_service_active(hostname, protocol="icmp"):

    # if protocol == "http":
    #     print("Chequeando via HTTP - no implementado")
    #     return False


    """
    Verifica si un host responde al ping.
    Retorna True si responde, False si no.
    """
    # Windows: f"ping -n 1 {hostname} > NUL 2>&1
    # Linux/macOS f"ping -c 1 {hostname} > /dev/null 2>&1
    command = f"ping -n 1 {hostname} > NUL 2>&1"

    response_code = os.system(command)

    # Si el código de respuesta es 0, el ping es exitoso.
    return response_code == 0

# Prueba manual para ver si funciona (es útil para entender el funcionamiento antes de aplicar el test)
if __name__ == "__main__":
    print(f"¿Está 'localhost' activo?: {is_service_active('localhost')}")
    print(f"¿Esté servicio activo?: {is_service_active('hostinventado123xyz.com')}")