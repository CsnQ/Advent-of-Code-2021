import pytest

from src.solutions.day6.day6pt2 import LanternfishSim2


class TestLanternfishSim:

    @pytest.fixture
    def basic_sim(self):
        return LanternfishSim2([3, 3, 2], 1)

    # expected_num_of_fish = 26
    @pytest.fixture
    def eighteen_day_sim(self):
        return LanternfishSim2([3, 4, 3, 1, 2], 18)

    @pytest.fixture
    def two_day_sim(self):
        return LanternfishSim2([3, 4, 3, 1, 2], 2)

    def test_initialise_dict(self, basic_sim):
        expected_result = {
            0: 0,
            1: 0,
            2: 1,
            3: 2,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }

        basic_sim._initialise_dictionary()
        assert basic_sim.frequency_dict == expected_result

    def test_execute_sim_for_one_day(self, basic_sim):
        basic_sim._initialise_dictionary()
        initial_values = {
            0: 0,
            1: 0,
            2: 1,
            3: 2,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }
        assert basic_sim.frequency_dict == initial_values

        expected_after_1_day = {
            0: 0,
            1: 1,
            2: 2,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
        }

        basic_sim._execute_sim_for_one_day()
        assert basic_sim.frequency_dict == expected_after_1_day

    def test_sim_eighteen_days(self, eighteen_day_sim):
        expected_num_of_fish = 26
        actual_result = eighteen_day_sim.run_sim()
        assert actual_result == expected_num_of_fish
