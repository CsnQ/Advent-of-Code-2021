from typing import List


def create_tuple_list_from_input(submarine_moves: List[str]) -> List[tuple]:
    directions = [tuple(move.split()) for move in submarine_moves]
    return directions


def calculate_position(directions: List[tuple]) -> int:
    position = {
        'horizontal': 0,
        'depth': 0,
        'aim': 0
    }

    for item in directions:
        if item[0] == 'forward':
            position['horizontal'] = position['horizontal'] + int(item[1])
        elif item[0] == 'up':
            position['depth'] = position['depth'] - int(item[1])
        elif item[0] == 'down':
            position['depth'] = position['depth'] + int(item[1])
        else:
            continue
    result = position['horizontal'] * position['depth']
    return result


def calculate_alt_position(directions: List[tuple]):
    position = {
        'horizontal': 0,
        'depth': 0,
        'aim': 0
    }
    for item in directions:
        x = position
        if item[0] == 'forward':
            position['horizontal'] = position['horizontal'] + int(item[1])
            position['depth'] += position['aim'] * int(item[1])
        elif item[0] == 'up':
            position['aim'] = position['aim'] - int(item[1])
        elif item[0] == 'down':
            position['aim'] = position['aim'] + int(item[1])
    result = position['horizontal'] * position['depth']
    return result


def get_part_1(submarine_moves: List[str]) -> int:
    result = calculate_position(create_tuple_list_from_input(submarine_moves))
    print(result)
    return result


def get_part_2(submarine_moves: List[str]) -> int:
    result = calculate_alt_position(create_tuple_list_from_input(submarine_moves))
    print(result)
    return result
