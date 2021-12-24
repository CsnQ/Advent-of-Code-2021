import pytest

from src.solutions.day6.lanternfish import Lanternfish


class TestLanternfish:

    @pytest.fixture
    def test_laternfish(self) -> Lanternfish:
        return Lanternfish(3, False)

    def test_lanternfish_countdown(self, test_laternfish):
        assert test_laternfish.time_to_reproduction == 3
        test_laternfish.take_away_day()
        assert test_laternfish.time_to_reproduction == 2

    def test_timer_reset(self,test_laternfish):
        assert test_laternfish.time_to_reproduction == 3
        test_laternfish.take_away_day()
        assert test_laternfish.time_to_reproduction == 2
        test_laternfish.take_away_day()
        assert test_laternfish.time_to_reproduction == 1
        test_laternfish.take_away_day()
        assert test_laternfish.time_to_reproduction == 0
        test_laternfish.take_away_day()
        assert test_laternfish.time_to_reproduction == 6





