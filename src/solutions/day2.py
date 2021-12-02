from typing import List

position = {
    'horizontal': 0,
    'depth': 0
}


def create_tuple_list_from_input(submarine_moves: List[str]) -> List[tuple]:
    directions = [tuple(move.split()) for move in submarine_moves]
    return directions


def calculate_position(directions: List[tuple]):
    for item in directions:
        if item[0] == 'forward':
            position['horizontal'] = position['horizontal'] + int(item[1])
        elif item[0] == 'up':
            position['depth'] = position['depth'] - int(item[1])
        elif item[0] == 'down':
            position['depth'] = position['depth'] + int(item[1])
        else:
            continue


def get_part_1(submarine_moves: List[str]) -> int:
    calculate_position(create_tuple_list_from_input(submarine_moves))
    result = position['horizontal']*position['depth']
    print(result)
    return result
