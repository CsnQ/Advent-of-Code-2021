import pytest

from src.solutions.day1 import get_part1_answer


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
