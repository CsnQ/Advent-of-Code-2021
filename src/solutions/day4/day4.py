from typing import List

from src.solutions.day4.bingo_card import BingoCard


class Day4:
    def __init__(self, bingo_calls_and_cards: List[str]):
        self.bingo_calls_and_cards = bingo_calls_and_cards
        self.raw_data = self.split_input()
        self.numbers_called = [int(number) for number in self.raw_data[0][0].split(',')]
        self.list_of_bingo_cards = [self.process_card(card) for card in self.raw_data[1:]]
        self.bingo_card_objects = self.create_bingo_card_objs()

    def split_input(self):
        # TODO: fix this. tis criminal and I copied it
        #  from the internet and its not very pythonic and very inefficient. horrific
        size = len(self.bingo_calls_and_cards)
        idx_list = [idx + 1 for idx, val in
                    enumerate(self.bingo_calls_and_cards) if val == '']

        res = [self.bingo_calls_and_cards[i: j] for i, j in
               zip([0] + idx_list, idx_list +
                   ([size] if idx_list[-1] != size else []))]

        for item in res:
            if item[-1] == '':
                item.remove('')

        return res

    @staticmethod
    def process_card(card):
        return [
            [int(number) for number in row.split()]
            for row in card
        ]

    def get_list_of_bingo_cards(self):
        print(self.list_of_bingo_cards)

    def create_bingo_card_objs(self) -> list[BingoCard]:
        bingo_card_objs = []
        for card in self.list_of_bingo_cards:
            bingo_card = BingoCard(card)
            bingo_card_objs.append(bingo_card)

        return bingo_card_objs

    def simulate_game(self):
        for number in self.numbers_called:
            for card in self.bingo_card_objects:
                card.update_boolean_dataframe(number)
                result = card.check_if_have_bingo()
                break




