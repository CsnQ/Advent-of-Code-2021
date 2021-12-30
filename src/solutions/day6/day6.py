from typing import List

from src.solutions.day6.lanternfish import Lanternfish

input = [1, 1, 1, 1, 2, 1, 1, 4, 1, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 3, 1, 1, 1, 5, 1, 3, 1, 4, 1, 2, 1, 1, 5, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 4, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 4, 1, 1, 1, 1, 3, 5, 1, 1, 2, 1, 1,
         1, 1, 4, 4, 1, 1, 1, 4, 1, 1, 4, 2, 4, 4, 5, 1, 1, 1, 1, 2, 3, 1, 1, 4, 1, 5, 1, 1, 1, 3, 1, 1, 1, 1, 5, 5,
         1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1, 2, 3, 1, 5, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1,
         4, 3, 1, 1, 4, 1, 5, 4, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 4, 5, 1, 1, 1, 1, 5, 4, 1, 3, 1, 1, 1, 1,
         4, 3, 3, 3, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 5, 1, 3, 1, 4, 3, 1, 3, 1, 5, 1, 1, 1, 1, 3, 1, 5,
         1, 2, 4, 1, 1, 4, 1, 4, 4, 2, 1, 2, 1, 3, 3, 1, 4, 4, 1, 1, 3, 4, 1, 1, 1, 2, 5, 2, 5, 1, 1, 1, 4, 1, 1, 1,
         1, 1, 1, 3, 1, 5, 1, 2, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 5, 1, 1, 5, 1, 2, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 3, 2, 4, 1, 1, 2, 1, 1, 3, 2]


def get_day6_part1():
    part1 = LanternfishSim(input, 80)
    part1.run_sim()


class LanternfishSim:
    def __init__(self, list_of_fish, days_to_sim):
        self.list_of_fish = list_of_fish
        self.days_to_sim = days_to_sim
        self.list_of_lanternFish = [self._create_lanternfish(x, False) for x in list_of_fish]

    def _create_lanternfish(self, timer_int: int, is_new_fish: bool) -> Lanternfish:
        return Lanternfish(timer_int, is_new_fish)

    def _sim_reproduction(self):
        new_fish = Lanternfish(8, True)
        self.list_of_lanternFish.append(new_fish)

    def _execute_sim_for_one_day(self) -> List[int]:
        for fish in self.list_of_lanternFish:
            if fish.is_new_fish:
                continue
            elif fish.time_to_reproduction == 0:
                self._sim_reproduction()
                fish.reset_timer()
            elif fish.time_to_reproduction != 0 and fish.is_new_fish is False:
                fish.take_away_day()

        for fish in self.list_of_lanternFish:
            if fish.is_new_fish:
                fish.is_new_fish = False

        return [fish.time_to_reproduction for fish in self.list_of_lanternFish]

    def run_sim(self) -> int:
        for x in range(self.days_to_sim):
            self._execute_sim_for_one_day()
        result = len(self.list_of_lanternFish)
        print(result)
        return result
