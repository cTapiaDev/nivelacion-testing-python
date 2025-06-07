import requests
import json

def trigger_ci_pipeline(branch, commit_sha, triggered_by):
    
    url = "https://httpbin.org/post"

    headers = {
        "Content-Type": "application/json",
        "X-CI-Token": "un-token-secreto-de-ejemplo"
    }

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
        response = requests.post(url, headers=headers, json=payload, timeout=5)
        response.raise_for_status()

        print(f"[TRIGGER] Respuesta recibida con status {response.status_code}")
        return response.json()
    
    except requests.exceptions.RequestException as err:
        print(f"[ERROR] No se puede disparar el pipeline: {err}")
        return None
    

if __name__ == "__main__":
    response_data = trigger_ci_pipeline("main", "a1b2c3d4", "devops_script")

    if response_data:
        print("Analizando la respuesta de httpbin -----")
        print(json.dumps(response_data, indent=2))