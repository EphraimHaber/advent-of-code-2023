from typing import Match
from regex_utils import get_digits_matches
from pprint import pprint


def get_surrounding_string(digit_match_input: Match, current_line: int, max_line_length: int, max_lines: int, data) -> str:
    surrounding_string = ""
    check_to_left = digit_match_input.span()[0] != 0
    check_to_right = digit_match_input.span()[1] != max_line_length
    check_above = current_line != 0
    check_below = current_line != max_lines

    # most_left_index = digit_match_input.span()[0] - int(check_to_left)
    most_left_index = digit_match_input.span()[0] - int(check_to_left)
    most_right_index = digit_match_input.span()[1] + int(check_to_right) + 1
    most_right_index = min(most_right_index, line_length - 1)
    surrounding_string += data[current_line][most_left_index]
    surrounding_string += data[current_line][most_right_index]

    if check_above:
        surrounding_string += data[current_line-1][most_left_index:most_right_index]
    if check_below:
        surrounding_string += data[current_line+1][most_left_index:most_right_index]
    return surrounding_string


if __name__ == '__main__':
    with open('puzzle.txt', 'r') as file:
        file_lines = file.read().split('\n')
        line_length = len(file_lines[0])
        final_sum = 0
        print(line_length)
        # file_lines = file_lines[1:2]
        for i, file_line in enumerate(file_lines):
            file_line: str = file_line
            # print(i, file_line)
            digits_matches = get_digits_matches(file_line)
            for digit_match in digits_matches:
                print(digit_match)
                current_surrounding_string = get_surrounding_string(digit_match, i, line_length, len(file_lines) - 1, file_lines)
                print(current_surrounding_string)
                current_surrounding_string = current_surrounding_string.replace('.', '')
                # current_surrounding_string = ''.join(filter(lambda z: not z.isdigit(), current_surrounding_string))
                for letter in current_surrounding_string:
                    if letter.isdigit():
                        current_surrounding_string = current_surrounding_string.replace(letter, '')
                if current_surrounding_string:
                    print(int(digit_match.group(0)))
                    print(int(digit_match.group(0)))
                    final_sum += int(digit_match.group(0))
        print("---------")
        print(final_sum)
