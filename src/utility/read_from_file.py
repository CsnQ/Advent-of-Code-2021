from typing import List


def read_list_from_file_as_int(file_path: str) -> List[int]:
    data_from_file = []
    with open(file_path) as file:
        for line in file:
            data_from_file.append(int(line.rstrip()))

    return data_from_file


def read_list_from_file_as_string(file_path: str) -> List[str]:
    data_from_file = []
    with open(file_path) as file:
        for line in file:
            data_from_file.append(line.rstrip())

    return data_from_file
