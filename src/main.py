from src.solutions.day1 import get_part1_answer, get_part2_answer
from src.solutions.day2 import get_part_1, get_part_2
from src.solutions.day3 import get_day3_part_1, get_day3_part_2
from src.solutions.day6.day6 import get_day6_part1
from src.utility.read_from_file import read_list_from_file_as_int, read_list_from_file_as_string


def run_puzzles():
    print("day 1 answers:")
    day1_input = read_list_from_file_as_int("input/day1/day_1_real_input.txt")
    get_part1_answer(day1_input)
    get_part2_answer(day1_input)
    print("*************************************************")

    print("day 2 answers:")
    day2_input = read_list_from_file_as_string("input/day2/day_2_real_input.txt")
    get_part_1(day2_input)
    get_part_2(day2_input)
    print("*************************************************")



    print("day 6 answers:")
    get_day6_part1()
    print("*************************************************")


if __name__ == '__main__':
    run_puzzles()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
