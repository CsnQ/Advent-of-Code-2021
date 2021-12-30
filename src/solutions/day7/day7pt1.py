from typing import List, Dict


def get_day7_part1(puzzle_input):
    return FuelCalculator(puzzle_input).get_part_1_answer()


class FuelCalculator:
    def __init__(self, puzzle_input: List[int]):
        self.crabs = puzzle_input

    def get_single_calculation(self, position) -> int:
        result = []
        for crab in self.crabs:
            fuel_cost = abs(crab - position)
            result.append(fuel_cost)
        return sum(result)

    def get_fuel_usage_for_position(self) -> Dict[int, int]:
        result = {}
        for crab in self.crabs:
            result[self.crabs.index(crab) + 1] = self.get_single_calculation(self.crabs.index(crab) + 1)

        return result

    def get_part_1_answer(self) -> int:
        calculation_result = self.get_fuel_usage_for_position()
        sorted_vals = list(calculation_result.values())
        sorted_vals.sort()
        print(sorted_vals[0])
        return sorted_vals[0]
