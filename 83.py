import functools

# Mock function to get current user permissions (you can replace this with actual logic)
def get_current_user_permissions():
    # Example permissions, replace with actual user permission fetching logic
    return ['admin', 'editor']

def requires_permission(permission):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_permissions = get_current_user_permissions()
            if permission in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError("You do not have permission to access this resource.")
        return wrapper
    return decorator

@requires_permission('admin')
def delete_user(user_id):
    print(f"User {user_id} deleted")

# Testing the function
try:
    delete_user(123)
except PermissionError as e:
    print(e)


print("Code written and executed by Kunsh Dhawan")