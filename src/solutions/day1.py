from typing import List


def get_part1_answer(depths: List) -> int:
    count = 0
    items_to_iterate = len(depths) - 1
    for i in range(items_to_iterate):
        if depths[i + 1] > depths[i]:
            count += 1

    print(count)
    return count


def get_part2_answer(depths: List) -> int:
    sublist = get_sublists(depths)
    totals = get_totals(sublist)
    answer = get_part1_answer(totals)
    return answer


def get_totals(sublist: List) -> List[int]:
    totals = []
    [totals.append(sum(x)) for x in sublist]
    return totals


def get_sublists(depths: List) -> List[List]:
    depth_sublist = []
    for i in range(len(depths)):
        if i + 3 == len(depths):
            sublist = depths[i:]
            depth_sublist.append(sublist)
            break
        elif i + 3 > len(depths):
            sublist = depths[i:]
            depth_sublist.append(sublist)
            break
        else:
            sublist = depths[i:i + 3]
            depth_sublist.append(sublist)

    return depth_sublist
