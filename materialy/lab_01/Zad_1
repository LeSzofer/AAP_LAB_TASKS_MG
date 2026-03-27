current_user = {"username": "admin", "role": "superuser"}

def require_role(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user.get("role") != role:
                raise PermissionError(
                    f"Access denied: required role '{role}', "
                    f"but current user has role '{current_user.get('role')}'"
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Przykład użycia:
@require_role("superuser")
def admin_panel():
    return "Welcome to admin panel!"

@require_role("user")
def user_panel():
    return "Not welcome user!"

print(admin_panel())  # działa, bo role = "superuser"

try:
    print(user_panel())
except PermissionError as e:
    print(f"Brak uprawnień: {e}")





