import pytest

from src.solutions.day7 import FuelCalculator


class TestDay7:

    @pytest.fixture
    def fuel_calc_with_test_input(self):
        return FuelCalculator([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])

    def test_find_min_and_max(self, fuel_calc_with_test_input):
        expected_result = (0, 16)
        actual_result = fuel_calc_with_test_input.find_min_and_max()
        assert expected_result == actual_result

    def test_get_single_calculation_position_2(self, fuel_calc_with_test_input):
        expected_result = 37
        actual_result = fuel_calc_with_test_input.get_single_calculation(2)
        assert expected_result == actual_result

    def test_get_single_calculation_position_10(self, fuel_calc_with_test_input):
        expected_result = 71
        actual_result = fuel_calc_with_test_input.get_single_calculation(10)
        assert expected_result == actual_result

    def test_get_fuel_usage_for_position(self, fuel_calc_with_test_input):
        expected_number_of_items = len(set(fuel_calc_with_test_input.crabs))
        result = fuel_calc_with_test_input.get_fuel_usage_for_position()
        assert expected_number_of_items == len(result.keys())
        assert result[2] == 37
        assert result[10] == 71
        assert result[3] == 39

    def test_get_part_1_answer(self, fuel_calc_with_test_input):
        expected_result = 37
        assert fuel_calc_with_test_input.get_part_1_answer() == expected_result
