from src.solutions.day4.bingo_card import BingoCard

test_card = [[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7],[6, 10,  3, 18,  5],
             [1, 12, 20, 15, 19]]


def test_bingo_card_data_frame_created():
    bingo_card = BingoCard(test_card)
    # print(bingo_card.bingo_card_dataframe)
    # print(bingo_card.bingo_card_boolean)
    bingo_card.update_dataframe(7)
    bingo_card.update_dataframe(9)
