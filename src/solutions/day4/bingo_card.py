from typing import List

import pandas as pd
from collections import Counter

from pandas import Series


class BingoCard:
    def __init__(self, bingo_card: List[list[int]]):
        self.bingo_card = bingo_card
        self.bingo_card_dataframe = pd.DataFrame(self.bingo_card)
        self.bingo_card_boolean = self.make_boolean_dataframe_from_card()
        self.bingo_card_total = self.bingo_card_dataframe.values.sum()
        self.winning_result =  None

    def make_boolean_dataframe_from_card(self):
        df = pd.DataFrame(index=range(5), columns=range(5))
        for i in range(0, 5):
            df[i] = False

        return df

    def update_boolean_dataframe(self, number: int):
        self.bingo_card_boolean = self.bingo_card_boolean | (self.bingo_card_dataframe == number)

    def calculate_winning_combo(self,winning_line: Series):
        print(self.bingo_card_dataframe)
        print(self.bingo_card_boolean)


    def check_if_have_bingo(self):
        for row in self.bingo_card_boolean.iterrows():
            if row[1].all():
                self.calculate_winning_combo(self.bingo_card_dataframe.loc[row[0]])
                return True

        for col in self.bingo_card_boolean.iteritems():
            if col[1].all():
                return self.bingo_card_dataframe.iloc[:, col[0]]
