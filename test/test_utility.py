from src.utility.read_from_file import read_list_from_file_as_int,\
    read_list_from_file_as_string


class TestUtility:
    def test_read_list_from_file(self):
        expected_result = [1, 2, 3]
        actual = read_list_from_file_as_int("resources/test_file.txt")
        assert actual == expected_result

    def test_read_list_from_file_as_string(self):
        expected_result = ['1', '2', '3']
        actual = read_list_from_file_as_string("resources/test_file.txt")
        assert actual == expected_result
