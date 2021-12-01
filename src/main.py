from src.solutions.day1 import get_part1_answer, get_part2_answer
from src.utility.read_from_file import read_list_from_file_as_int


def run_puzzles():
    input = read_list_from_file_as_int("input/day1_part1_real_input.txt")
    get_part1_answer(input)
    get_part2_answer(input)

if __name__ == '__main__':
    run_puzzles()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
