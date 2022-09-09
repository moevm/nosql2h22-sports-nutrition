import functools
from dataclasses import dataclass
from logging import basicConfig, DEBUG, debug


@dataclass
class LoggerConstants:
    LOGGER_FILE_NAME: str = "sports-nutrition.log"


def configure_logging():
    basicConfig(filename=LoggerConstants.LOGGER_FILE_NAME, level=DEBUG, force=True)


def is_logged(names: list = [], level=debug):
    def is_logged_decorator(func):
        @functools.wraps(func)
        def wrapper_is_logged(*args, **kwargs):
            signature = parse_signature(names, " ,", args, kwargs)
            level(f"Calling {func.__name__}({signature})")
            value = func(*args, **kwargs)
            level(f"{func.__name__} result: {value}")
            return value

        return wrapper_is_logged

    return is_logged_decorator


def parse_signature(names: list, pattern: str, *args, **kwargs):
    args_repr = list(f"{repr(names[i])}: {args[0][i]}" for i in range(0, len(names)))
    kwargs_repr = list(f"{k}={v!r}" for k, v in kwargs.items())
    return pattern.join(args_repr + kwargs_repr)
