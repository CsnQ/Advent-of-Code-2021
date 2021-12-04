from src.solutions.day3 import create_vertical_list, get_frequencies, get_rate, convert_binary_to_int, \
    convert_gamma_and_epsilon, calculate_energy_consumption, get_day3_part_1, get_oxygen_value, get_day3_part_2


class TestDay3:
    # 00100
    # 11110
    def test_create_vertical_list(self):
        test_data = ['00100', '11110']

        expected_result = ['01', '01', '11', '01', '00']

        actual_result = create_vertical_list(test_data)
        assert actual_result == expected_result

    def test_get_frequencies(self):
        test_data = ['011', '000']
        expected_result = {
            0: {'0': 1,
                '1': 2,
                'most_common_digit': 1,
                'least_common_digit': 0
                },
            1: {'0': 3,
                '1': 0,
                'most_common_digit': 0,
                'least_common_digit': 1
                }
        }

        actual_result = get_frequencies(test_data)
        assert actual_result == expected_result

    def test_get_gamma_and_epsilon_rate(self):
        test_data = {
            0: {'0': 1,
                '1': 2,
                'most_common_digit': 1,
                'least_common_digit': 0
                },
            1: {'0': 3,
                '1': 0,
                'most_common_digit': 0,
                'least_common_digit': 1
                }}

        expected_result = [1, 0]
        actual_result = get_rate(test_data, 'most_common_digit')
        assert actual_result == expected_result

        expected_result = [0, 1]
        actual_result = get_rate(test_data, 'least_common_digit')
        assert actual_result == expected_result

    def test_convert_to_int(self):
        test_data = [1, 0, 1]
        expected_result = 5
        actual_result = convert_binary_to_int(test_data)
        assert expected_result == actual_result

    # 10110 = 22
    # 01001=9
    def test_convert_gamma_and_epsilon(self):
        test_data = ([1, 0, 1, 1, 0], [0, 1, 0, 0, 1])
        expected_result = (22, 9)
        actual_result = convert_gamma_and_epsilon(test_data)
        assert expected_result == actual_result

    def test_get_energy_consumption(self):
        test_data = (22, 9)
        expected_result = 198
        actual_result = calculate_energy_consumption(test_data)
        assert expected_result == actual_result

    def test_get_test_get_part_1(self):
        test_data = ['00100',
                     '11110',
                     '10110',
                     '10111',
                     '10101',
                     '01111',
                     '00111',
                     '11100',
                     '10000',
                     '11001',
                     '00010',
                     '01010']
        expected_result = 198
        actual_result = get_day3_part_1(test_data)
        assert expected_result == actual_result

    def test_get_oxygen_value(self):
        test_data = ['00100',
                     '11110',
                     '10110',
                     '10111',
                     '10101',
                     '01111',
                     '00111',
                     '11100',
                     '10000',
                     '11001',
                     '00010',
                     '01010']
        expected_result = '10111'
        actual_result = get_oxygen_value(test_data)
        assert expected_result == actual_result

    def test_get_result(self):
        test_data = ['00100',
                     '11110',
                     '10110',
                     '10111',
                     '10101',
                     '01111',
                     '00111',
                     '11100',
                     '10000',
                     '11001',
                     '00010',
                     '01010']
        expected_result = 230
        actual_result = get_day3_part_2(test_data)
        assert expected_result == actual_result
