import pytest

def test_legacy_backup_script():
    """
    Simula la prueba de un script de backup antiguo que ya no se usa mucho,
    pero que aún pasa porque no lo queremos eliminar.
    """
    assert True

@pytest.mark.skip(reason="Funcionalidad de deploy a Kubernetes aún no implementadas en el script principal.")
def test_deploy_to_kubernetes_v2():
    """
    Esta prueba contendrá una nueva funcionalidad de despliegue que no está lista.
    La saltamos para que no falle en el CI.
    """
    assert False; "Esta prueba fallaría si se ejecutara porque la función no está lista"


@pytest.mark.xfail(reason="Se sabe que la API externa tiene un bug actualmente.")
def test_check_external_monitoring_api():
    """
    Aquí verificamos la integración con una API externa que sabemos que falla.
    Esperamos que falle, pero que no afecte la ejecución de los test.
    """
    external_api_is_ok = True
    assert external_api_is_ok, "La API externa de monitoreo no respondió como se esperaba."


@pytest.mark.xfail(strict=True, reason="Este test va a fallar. Si pasa, es un problema.")
def test_critical_security():
    """
    A veces, podemos querer que una prueba falle si la configuración de seguridad crítica
    no está forzando un error como debería.
    Si la prueba pasa, es una alerta.
    """
    assert not True, "La configuración de seguridad es demasiado permisiva."
    # El strict=True permite que si la prueba llega a pasar, aun siendo un XPASS, genera un error en el reporte.