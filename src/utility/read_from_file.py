from typing import List


def read_list_from_file(file_path: str) -> List:
    data_from_file = []
    with open(file_path) as file:
        for line in file:
            print(line.rstrip())
            data_from_file.append(line.rstrip())

    return data_from_file
