def add_system_user(username):
    if not username:
        return False
    print(f"Usuario {username} añadido al sistema.")
    return True

def remove_system_user(username):
    if not username:
        return False
    print(f"Usuario {username} eliminado del sistema.")
    return True