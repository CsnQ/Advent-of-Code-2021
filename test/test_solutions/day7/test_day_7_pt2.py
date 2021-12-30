import pytest

from src.solutions.day7.day7pt2 import FuelCalculator2


class TestDay7:

    @pytest.fixture
    def fuel_calc_with_test_input(self):
        return FuelCalculator2([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])

    def test_get_single_calculation_position_5(self, fuel_calc_with_test_input):
        expected_result = 168
        actual_result = fuel_calc_with_test_input.get_single_calculation(5)
        assert actual_result == expected_result

    def test_get_single_calculation_position_2(self, fuel_calc_with_test_input):
        expected_result = 206
        actual_result = fuel_calc_with_test_input.get_single_calculation(2)
        assert expected_result == actual_result

    def test_get_fuel_usage_for_position(self, fuel_calc_with_test_input):
        expected_number_of_items = len(set(fuel_calc_with_test_input.crabs))
        result = fuel_calc_with_test_input.get_fuel_usage_for_position()
        assert expected_number_of_items == len(result.keys())
        assert result[5] == 168
        assert result[2] == 206

    def test_get_part_2_answer(self, fuel_calc_with_test_input):
        expected_result = 168
        assert fuel_calc_with_test_input.get_part_2_answer() == expected_result
