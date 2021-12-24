import pytest

from src.solutions.day6.day6 import LanternfishSim


class TestLanternfishSim:

    @pytest.fixture
    def basic_sim(self):
        return LanternfishSim([3, 2], 1)

    @pytest.fixture
    def multi_day_sim(self):
        return LanternfishSim([3, 4, 3, 1, 2], 2)

    @pytest.fixture
    def eighty_day_sim(self):
        return LanternfishSim([3, 4, 3, 1, 2], 80)

    def test_object(self, basic_sim):
        assert basic_sim.days_to_sim == 1
        assert basic_sim.list_of_lanternFish[0].time_to_reproduction == 3
        assert basic_sim.list_of_lanternFish[0].is_new_fish is False
        assert basic_sim.list_of_lanternFish[1].time_to_reproduction == 2
        assert basic_sim.list_of_lanternFish[0].is_new_fish is False

    def test_execute_sim_for_one_day(self, multi_day_sim):
        day_1 = multi_day_sim._execute_sim_for_one_day()
        print(day_1)
        assert day_1 == [2, 3, 2, 0, 1]
        day_2 = multi_day_sim._execute_sim_for_one_day()
        print(day_2)
        assert day_2 == [1, 2, 1, 6, 0, 8]

    def test_run_sim_18_days(self):
        eighteen_day_sim = LanternfishSim([3, 4, 3, 1, 2], 18)
        expected_num_of_fish = 26
        assert eighteen_day_sim.run_sim() == expected_num_of_fish

    def test_run_sim_80_days(self, eighty_day_sim):
        expected = 5934
        assert eighty_day_sim.run_sim() == expected
