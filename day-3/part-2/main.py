from typing import Tuple
from regex_utils import get_asterisks_matches


def get_numbers_row_col_offset(lines: list[str]) -> list[Tuple[int, int]]:
    locs = []
    for i, curr_line in enumerate(lines):
        for j, char in enumerate(curr_line):
            if char.isdigit():
                locs.append((i - 1, j - 1))
    return locs


def get_filtered_line(temp_line: str) -> str:
    res = [c for c in temp_line]
    replace = []
    for i in range(1, len(res)):
        if res[i].isdigit() and res[i - 1].isdigit():
            replace.append(i)
    for index in replace:
        res[index] = '.'
    return "".join(res)


def walk_number(num_row: int, num_col: int) -> int:
    checking_line: str = file_lines[num_row]
    start_index = num_col
    while checking_line[start_index].isdigit():
        start_index -= 1
        if not checking_line[start_index].isdigit():
            start_index += 1
            break
    buffer = ''
    while checking_line[start_index].isdigit():
        buffer += checking_line[start_index]
        start_index += 1
        if not 0 <= start_index <= len(checking_line) - 1:
            break
        if not checking_line[start_index].isdigit():
            break
    return int(buffer)


if __name__ == '__main__':
    with open('puzzle.txt', 'r') as file:
        total = 0
        file_lines = file.read().split('\n')
        for line_index, file_line in enumerate(file_lines):
            file_line: str
            matches = get_asterisks_matches(file_line)
            for match in matches:
                row = line_index
                col = match.span()[0]

                line_above = file_lines[row - 1][col - 1:match.span()[1] + 1]
                current_line = file_lines[row][col - 1:match.span()[1] + 1]
                line_below = file_lines[row + 1][col - 1:match.span()[1] + 1]

                current_lines = [line_above, current_line, line_below]
                current_lines = [get_filtered_line(line) for line in current_lines]
                nums_location = get_numbers_row_col_offset(current_lines)
                if len(nums_location) != 2:
                    continue
                num1_row = nums_location[0][0] + line_index
                num1_col = nums_location[0][1] + col
                num2_row = nums_location[1][0] + line_index
                num2_col = nums_location[1][1] + col
                total += walk_number(num1_row, num1_col) * walk_number(num2_row, num2_col)
        print(total)  # 84584891
