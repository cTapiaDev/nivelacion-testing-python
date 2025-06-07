import requests
import json

def trigger_ci_pipeline(branch, commit_sha, triggered_by):
    """
    Simula el disparo de un pipeline de CI enviando datos a httpbin
    """
    url = "https://httpbin.org/post"


    # En un caso real, un token de API iría aquí para la autenticación.
    headers = {
        "Content-Type": "application/json",
        "X-CI-Token": "un-token-secreto-de-ejemplo"
    }

    # 'payload' son los datos que enviamos en el cuerpo de la petición POST.
    payload = {
        "branch": branch,
        "commit": commit_sha,
        "variables": {
            "DEPLOY_TARGET": "staging",
            "TRIGGERED_BY_SCRIPT": "True"
        },
        "triggered_by": triggered_by
    }
    print(f"[TRIGGER] Payload a enviar: {payload}")

    try:
        # requests.post envía los datos.
        # Con json=payload el requests se encarga de convertir el payload en una cadena de texto JSON.
        # También añade automáticamente el header 'Content-Type: application/json"
        response = requests.post(url, headers=headers, json=payload, timeout=5)
        response.raise_for_status()

        print(f"[TRIGGER] Respuesta recibida con status {response.status_code}")
        # Devolvemos la respuesta para poder inspeccionarla.
        return response.json()
    
    except requests.exceptions.RequestException as err:
        print(f"[ERROR] No se puede disparar el pipeline: {err}")
        return None
    

if __name__ == "__main__":
    response_data = trigger_ci_pipeline("main", "a1b2c3d4", "devops_script")

    if response_data:
        print("Analizando la respuesta de httpbin -----")
        print(json.dumps(response_data, indent=2)) #json.dumps con ident=2 formatea la salida para que sea legible.