from typing import List, Dict


def get_day7_part2(puzzle_input):
    return FuelCalculator2(puzzle_input).get_part_2_answer()


class FuelCalculator2:
    def __init__(self, puzzle_input: List[int]):
        self.crabs = puzzle_input

    def get_single_calculation(self, position) -> int:
        result = []
        for crab in self.crabs:
            moves = abs(crab - position)
            fuel_cost = 0
            current_cost = 0
            for x in range(moves):
                fuel_cost += 1
                current_cost = current_cost + fuel_cost

            result.append(current_cost)
        return sum(result)

    def get_fuel_usage_for_position(self) -> Dict[int, int]:
        result = {}
        for crab in self.crabs:
            result[self.crabs.index(crab) + 1] = self.get_single_calculation(self.crabs.index(crab) + 1)

        return result

    def get_part_2_answer(self) -> int:
        calculation_result = self.get_fuel_usage_for_position()
        sorted_vals = list(calculation_result.values())
        sorted_vals.sort()
        print(sorted_vals[0])
        return sorted_vals[0]
