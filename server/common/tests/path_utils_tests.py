import unittest

from server.common.exceptions import FileNotFound
from server.common.path_utils import check_path_exists


class PathTestCase(unittest.TestCase):
    def test_check_path_exists_not_existing_file_raises_exception(self):
        with self.assertRaises(FileNotFound):
            check_path_exists('exception')

    def test_check_path_exists_file_present_no_exception_raised(self):
        path = "./resources/test.json"
        self.assertEqual(path, check_path_exists(path))


if __name__ == '__main__':
    unittest.main()
