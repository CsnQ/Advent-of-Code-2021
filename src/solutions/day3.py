from typing import List


def create_vertical_list(digits: List[str]) -> List[str]:
    # I know that all the digits are the same length in my data set otherwise
    # I would be more sophisticated here
    digit_len = len(digits[0])
    vertical_list = []
    for i in range(0, digit_len):
        number = ''
        for digit in digits:
            number += digit[i]
        vertical_list.append(number)

    return vertical_list


def get_frequencies(vertical_list: List[str]) -> dict[int, dict[str, int]]:
    frequency_matrix = {}
    for item in vertical_list:
        current_key = vertical_list.index(item)
        frequency_matrix[current_key] = {'0': 0, '1': 0,
                                         'most_common_digit': 0,
                                         'least_common_digit': 1}
        zero_counter = 0
        one_counter = 0
        for digit in item:
            if digit == '0':
                zero_counter += 1
            elif digit == '1':
                one_counter += 1
            else:
                continue

        frequency_matrix[current_key]['0'] = zero_counter
        frequency_matrix[current_key]['1'] = one_counter
        if one_counter > zero_counter:
            frequency_matrix[current_key]['most_common_digit'] = 1
            frequency_matrix[current_key]['least_common_digit'] = 0

    return frequency_matrix


def get_rate(frequency_matrix: dict[int, dict[str, int]], rate: str) -> List[int]:
    result = []
    for key in frequency_matrix.keys():
        result.append(frequency_matrix[key][rate])

    return result


def convert_to_int(list_of_bits: list[int]) -> int:
    string_ints = [str(bit) for bit in list_of_bits]
    str_of_ints = "".join(string_ints)
    return int(str_of_ints, 2)


def convert_gamma_and_epsilon(bits: tuple) -> tuple:
    gamma_int = convert_to_int(bits[0])
    epsilon_int = convert_to_int(bits[1])
    return gamma_int, epsilon_int


def calculate_energy_consumption(ints: tuple) -> int:
    return ints[0] * ints[1]


def get_day3_part_1(digits: List[str]):
    vertical_list = create_vertical_list(digits)
    frequencies = get_frequencies(vertical_list)
    gamma_bits = get_rate(frequencies, 'most_common_digit')
    epsilon_bits = get_rate(frequencies, 'least_common_digit')
    converted_values = convert_gamma_and_epsilon((gamma_bits, epsilon_bits))
    result = calculate_energy_consumption(converted_values)
    print(result)
    return result
