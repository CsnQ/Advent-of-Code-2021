import pytest

from src.utility.read_from_file import read_list_from_file


class TestUtility:
    def test_read_list_from_file(self):
        expected_result = ['1', '2', '3']
        actual = read_list_from_file("resources/test_file.txt")
        assert actual == expected_result
