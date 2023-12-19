from pprint import pprint


def assert_all_lines_are_at_equal_length(lines: list[list[int]], line_length: int):
    for line in lines:
        assert len(line) == line_length


def get_diffs(nums: list[int]) -> list[int]:
    return [nums[i] - nums[i - 1] for i in range(1, len(nums))]


def generate_diffs(nums: list[int]) -> list[list[int]]:
    diffs = [nums]
    while any(x != 0 for x in nums):
        nums = get_diffs(nums)
        diffs.append(nums)
    return diffs


def walk_diffs(diffs: list[list[int]]) -> int:

    diffs.reverse()

    assert all(x == 0 for x in diffs[0])
    diffs[0].insert(0, 0)

    for i in range(1, len(diffs)):
        # print(f'{diffs[i][0]} - {diffs[i - 1][0]} = {diffs[i][0] - diffs[i - 1][0]}')
        diffs[i].insert(0, diffs[i][0] - diffs[i - 1][0])
    return diffs[-1][0]


def main():
    with open('puzzle.txt') as file:
        lines = [list(map(int, line.split())) for line in file.read().split('\n')]
        line_length = len(lines[0])
        assert_all_lines_are_at_equal_length(lines, line_length)
        res = 0
        for line in lines:
            temp = generate_diffs(line)
            projection = walk_diffs(temp)
            res += projection
        print('='*8)
        print(res)  # 973
        print('='*8)


if __name__ == '__main__':
    main()
