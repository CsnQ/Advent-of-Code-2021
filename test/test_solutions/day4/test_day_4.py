import pytest

from src.solutions.day4.day4 import Day4
from src.utility.read_from_file import read_list_from_file_as_string


@pytest.fixture
def under_test():
    day4 = Day4(read_list_from_file_as_string("../../resources/test_file2.txt"))
    return day4


class TestDay4:

    def test_check_attributes(self, under_test):
        expected_called_numbers = ['7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1']
        expected_bingo_cards = [['22 13 17 11  0', ' 8  2 23  4 24', '21  9 14 16  7', ' 6 10  3 18  5',
                                 ' 1 12 20 15 19'],
                                [' 3 15  0  2 22', ' 9 18 13 17  5', '19  8  7 25 23', '20 11 10 24  4',
                                 '14 21 16 12  6'],
                                ['14 21 17 24  4', '10 16 15  9 19', '18  8 23 26 20', '22 11 13  6  5',
                                 ' 2  0 12  3  7']]

        # assert expected_bingo_cards == under_test.list_of_bingo_cards
        # assert expected_called_numbers == under_test.numbers_called
        print(under_test.list_of_bingo_cards)

    def test_create_bingo_card_objs(self, under_test):
        result = under_test.bingo_card_objects
        # assert len(result) == 3
        # assert len(result[0]) == 2
        under_test.simulate_game()


