from typing import List


def get_part1_answer(depths: List) -> int:
    count = 0
    items_to_iterate = len(depths) - 1
    for i in range(items_to_iterate):
        if depths[i + 1] > depths[i]:
            count += 1

    print(count)
    return count


