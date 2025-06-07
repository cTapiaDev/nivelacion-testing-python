from user_utils import add_system_user, remove_system_user

class TestUserLifecycle: # El nombre de la clase debe comenzar con 'Test'
    """
    Agrupamos pruebas relacionadas con el ciclo de vida de los usuarios.
    """
    def test_can_add_valid_user(self): # Todas las funciones de prueba dentro de una clase, llevan el atributo 'self'
        """ Prueba para añadir un usuario con un nombre válido. """
        username = "testUser1"
        assert add_system_user(username) == True, f"Se esperaba poder añadir al usuario {username}"

    def test_can_remove_existing_user(self):
        """ Prueba para eliminar un usuario. """
        username = "testUser1"
        assert remove_system_user(username) == True, f"Se esperaba poder eliminar al usuario {username}"
    
def test_standalone():
    print("Ejecutando: test_standalone")
    assert True