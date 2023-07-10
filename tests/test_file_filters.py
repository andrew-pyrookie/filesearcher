# test_file_filters.py
import unittest
from file_searcher.file_filters import by_name, by_extension, by_content, by_size, by_modified_time

class FileFiltersTestCase(unittest.TestCase):
    def test_by_name(self):
        # Test casesfor the `by_name` function

    def test_by_name(self):
        dir = "/path/to/directory"
        name = "myfile.txt"
        expected_result = ["/path/to/directory/myfile.txt"]
        result = by_name(name, dir)
        self.assertEqual(result, expected_result)

        # Add more test cases as needed

    def test_by_name_no_match(self):
        dir = "/path/to/directory"
        name = "nonexistent.txt"
        expected_result = []
        result = by_name(name, dir)
        self.assertEqual(result, expected_result)

        # Add more test cases as needed


class FileFiltersTestCase(unittest.TestCase):
    def test_by_extension(self):
        # Test cases
        pass

    def test_by_extension_no_match(self):
        # Test cases
        pass

    # Add similar test methods for other file filter functions


if __name__ == '__main__':
    unittest.main()
