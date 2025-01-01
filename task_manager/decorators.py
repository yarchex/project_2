import functools
import logging

def log_action(action):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f"{action} вызван для функции {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator
