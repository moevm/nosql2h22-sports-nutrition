import unittest

from server.common.logger import is_logged


@is_logged(["string", "test", "primitive"])
def test_function(string: str, array: list, primitive: int, ignored):
    return "hello"


@is_logged()
def no_args_function():
    return "test"


@is_logged(["string"])
def default_args_function(string: str, default=None):
    return string


class IsLoggedTestCases(unittest.TestCase):
    def test_function_without_arguments_no_exception(self):
        no_args_function()

    def test_function_with_default_args(self):
        default_args_function("test")

    def test_function_with_arguments_ignore_one(self):
        test_function("1", [1], 1, 2)


if __name__ == '__main__':
    unittest.main()
