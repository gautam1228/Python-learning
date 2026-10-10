from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Log before the function")
        func()
        print("Log after the function")

    return wrapper


@my_decorator
def greet():
    print("Hello from decorators class from chaicode")


greet()
print(greet.__name__)  # without functools.wraps it gives the name as wrapper
