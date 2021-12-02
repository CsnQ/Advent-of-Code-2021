from src.solutions.day2 import create_tuple_list_from_input, get_part_1, get_part_2


class TestDay2:
    def test_create_tuple_list_from_input(self):
        test_data = ['forward 5',
                     'down 5', ]

        expected_result = [('forward', '5'),
                           ('down', '5')]

        actual_result = create_tuple_list_from_input(test_data)
        assert actual_result == expected_result

    def test_get_part_1(self):
        test_data = ['forward 5',
                     'down 5',
                     'forward 8',
                     'up 3',
                     'down 8',
                     'forward 2']

        expected_result = 150
        actual_result = get_part_1(test_data)
        assert actual_result == expected_result

    def test_get_part_2(self):
        test_data = ['forward 5',
                     'down 5',
                     'forward 8',
                     'up 3',
                     'down 8',
                     'forward 2']

        expected_result = 900
        actual_result = get_part_2(test_data)
        assert actual_result == expected_result