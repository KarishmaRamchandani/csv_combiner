import unittest
import error_codes
import io
import os

from unittest.mock import patch
from csv_combiner import CsvCombiner

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

"""
Unit tests for Csv Combiner
"""


class TestCsvCombiner(unittest.TestCase):

    def test_validate_valid_input(self):
        """
        TC 1 - Validate if validate method works with correct file name
        """
        input = [os.path.join(CURRENT_DIR, "test_files", "file1.csv")]
        combiner = CsvCombiner()
        combiner.validate(input)

    def test_validate_invalid_input(self):
        """
        TC 2 - Validate if validate method works returns False with incorrect file name
        """
        input = [os.path.join(CURRENT_DIR, "test_files", "file1.cs")]
        combiner = CsvCombiner()
        with self.assertRaises(Exception) as context:
            combiner.validate(input)
            self.assertTrue(
                error_codes.INVALID_INPUT_PATH in context.exception)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combine_files_valid_input(self, stdout):
        """
        TC 3 - Validate whether files are combined if file name and path is correct 
        """
        input = [os.path.join(CURRENT_DIR, "test_files", "file1.csv"), os.path.join(
            CURRENT_DIR, "test_files", "file2.csv")]
        combiner = CsvCombiner()
        combiner.combine(input)
        with open(os.path.join(CURRENT_DIR, "test_files", "combined.csv"), 'r') as file:
            expected = file.read()
        assert expected in stdout.getvalue()

    def test_combine_file_no_input(self):
        """
        TC 4 - Validate error when no input is given in file name 
        """
        input = []
        combiner = CsvCombiner()
        with self.assertRaises(Exception) as context:
            combiner.combine(input)

            self.assertTrue(
                error_codes.NO_INPUT_ARGUMENTS in context.exception)

    def test_combine_file_invalid_input(self):
        """
        TC 5 - Validate error when incorrect file name is given in file name 
        """
        input = [os.path.join(CURRENT_DIR, "test_files",
                              "file1_not_present.csv")]
        combiner = CsvCombiner()
        with self.assertRaises(Exception) as context:
            combiner.combine(input)
            self.assertTrue(
                error_codes.INVALID_INPUT_PATH in context.exception)

    def test_combine_file_empty(self):
        """
        TC 6 - Validate error when empty file is given in file name 
        """
        input = [os.path.join(CURRENT_DIR, "test_files", "file3_empty.csv")]

        combiner = CsvCombiner()
        with self.assertRaises(Exception) as context:
            combiner.combine(input)
            self.assertTrue(
                error_codes.EMPTY_FILE_EXCEPTION in context.exception)


if __name__ == '__main__':
    unittest.main()
