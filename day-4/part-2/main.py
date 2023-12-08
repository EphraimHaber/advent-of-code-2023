import math


def get_number_of_matches(winning: list[str], guess_input: list[str]) -> int:
    return len([num for num in guess_input if num in winning and num.strip()])


def convert_string_to_string_array(number_set: str) -> list[str]:
    number_set = number_set.replace('  ', ' ')
    number_set = number_set.split(' ')
    return number_set


if __name__ == '__main__':
    value = 0
    total_num_of_cards = 0
    with open('puzzle.txt', 'r') as file:
        file_lines = file.read().split('\n')
        histogram = [1 for line in file_lines]
        for line_index, line in enumerate(file_lines):
            line = line.split(':')[1]
            winning_numbers = line.split('|')[0]
            guess = line.split('|')[1]
            winning_numbers = convert_string_to_string_array(winning_numbers)
            guess = convert_string_to_string_array(guess)

            total = get_number_of_matches(winning_numbers, guess)
            while histogram[line_index] > 0:
                total_num_of_cards += 1
                for i in range(total):
                    histogram[line_index + 1 + i] += 1
                histogram[line_index] -= 1

        print(total_num_of_cards)

