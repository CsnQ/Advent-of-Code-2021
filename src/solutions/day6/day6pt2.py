import collections

input = [1, 1, 1, 1, 2, 1, 1, 4, 1, 4, 3, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 3, 1, 1, 1, 5, 1, 3, 1, 4, 1, 2, 1, 1, 5, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 4, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 4, 1, 1, 1, 1, 3, 5, 1, 1, 2, 1, 1,
         1, 1, 4, 4, 1, 1, 1, 4, 1, 1, 4, 2, 4, 4, 5, 1, 1, 1, 1, 2, 3, 1, 1, 4, 1, 5, 1, 1, 1, 3, 1, 1, 1, 1, 5, 5,
         1, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1, 1, 2, 3, 1, 5, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1,
         4, 3, 1, 1, 4, 1, 5, 4, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 4, 5, 1, 1, 1, 1, 5, 4, 1, 3, 1, 1, 1, 1,
         4, 3, 3, 3, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 5, 1, 3, 1, 4, 3, 1, 3, 1, 5, 1, 1, 1, 1, 3, 1, 5,
         1, 2, 4, 1, 1, 4, 1, 4, 4, 2, 1, 2, 1, 3, 3, 1, 4, 4, 1, 1, 3, 4, 1, 1, 1, 2, 5, 2, 5, 1, 1, 1, 4, 1, 1, 1,
         1, 1, 1, 3, 1, 5, 1, 2, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 5, 1, 1, 5, 1, 2, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 3, 2, 4, 1, 1, 2, 1, 1, 3, 2]

def get_day6_part2():
    part1 = LanternfishSim2(input, 256)
    part1.run_sim()

class LanternfishSim2:
    def __init__(self, list_of_fish, days_to_sim):
        self.list_of_fish = list_of_fish
        self.days_to_sim = days_to_sim
        self.frequency_dict = \
            {
                0: 0,
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0,
                8: 0
            }
        self.number_frequency = dict(collections.Counter(list_of_fish))
        self.standard_time_for_reproduction = 6
        self.new_fish_time_for_reproduction = 8

    def _initialise_dictionary(self):
        for key in self.number_frequency:
            self.frequency_dict[key] = self.number_frequency[key]

    def _execute_sim_for_one_day(self) -> dict:
        new_frequency_dict = \
            {
                0: 0,
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 0,
                8: 0
            }
        for item in range(1, 9):
            if self.frequency_dict[item] != 0:
                previous_key = item - 1
                current_value = self.frequency_dict[item]
                new_frequency_dict[previous_key] += current_value

        if self.frequency_dict[0] != 0:
            new_frequency_dict[8] += self.frequency_dict[0]
            new_frequency_dict[6] += self.frequency_dict[0]
        return new_frequency_dict

    def run_sim(self) -> int:
        self._initialise_dictionary()
        for x in range(self.days_to_sim):
            self.frequency_dict = self._execute_sim_for_one_day()

        values = self.frequency_dict.values()
        print(sum(values))
        return sum(values)
