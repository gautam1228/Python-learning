from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling the function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} the result: {result}")

    return wrapper


@logger
def add(a, b):
    return a + b


add(3, 5)
