from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied. Admins only.")
            return None
        else:
            return func(user_role)

    return wrapper


@require_admin
def view_sales_data(user_role):
    print("Sales data: [100, 200, 300]")


view_sales_data("admin")  # This will print the sales data
view_sales_data("user")  # This will print "Access denied. Admins only."
