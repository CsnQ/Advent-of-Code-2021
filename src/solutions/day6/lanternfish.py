class Lanternfish:
    def __init__(self, time_to_reproduction: int, is_new_fish: bool):
        self.time_to_reproduction = time_to_reproduction
        self.is_new_fish = is_new_fish

    def take_away_day(self):
        if self.time_to_reproduction == 0:
            self.reset_timer()
        else:
            self.time_to_reproduction -= 1

    def reset_timer(self):
        self.time_to_reproduction = 6

