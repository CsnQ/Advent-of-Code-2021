import pytest

from src.solutions.day1 import get_part1_answer, get_sublists, get_totals, get_part2_answer


class TestDay1:
    def test_get_part1_answer(self):
        input = [199,
                 200,
                 208,
                 210,
                 200,
                 207,
                 240,
                 269,
                 260,
                 263]

        result = get_part1_answer(input)
        assert result == 7

    def test_get_sublists(self):
        test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        expected = [[199, 200, 208],
                    [200, 208, 210],
                    [208, 210, 200],
                    [210, 200, 207],
                    [200, 207, 240],
                    [207, 240, 269],
                    [240, 269, 260],
                    [269, 260, 263]
                    ]
        result = get_sublists(test_data)
        assert result == expected

    def test_get_totals(self):
        test_data = [[2, 2, 2], [10, 20, 30]]
        expected = [6, 60]
        result = get_totals(test_data)
        assert result == expected

    def test_get_part2_answer(self):
        test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        expected = 5
        result = get_part2_answer(test_data)
        assert result == expected
