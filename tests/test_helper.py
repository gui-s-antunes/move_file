import unittest

from utils.helper import verify_file, verify_directory, get_time


class HelperTests(unittest.TestCase):

    def test_path_exist(self):
        self.assertTrue(
            verify_file('C:/Users/gui_s/PycharmProjects/move_file/app.py'), True
        )

    def test_path_not_exist(self):
        self.assertFalse(
            verify_file('C:/Users/gui_s/PycharmProjects/move_file/app222.py'), False
        )


if __name__ == '__main__':
    unittest.main()
