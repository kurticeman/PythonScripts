from time import time


def performance(function):
    def wrapper(*args, **kwargs):
        t_start = time()
        result = function(*args, **kwargs)
        t_end = time()
        print(f"took {t_end - t_start} ms")
        return result

    return wrapper
