from user_utils import add_system_user, remove_system_user

class TestUserLifecycle:

    def test_can_add_valid_user(self):
        username = "testUser1"
        assert add_system_user(username) == True, f"Se esperaba poder añadir al usuario {username}"

    def test_can_remove_existing_user(self):
        username = "testUser1"
        assert remove_system_user(username) == True, f"Se esperaba poder eliminar al usuario {username}"
    
def test_standalone():
    print("Ejecutando: test_standalone")
    assert True