from typing import Generator


def get_first_last_digits(config: str) -> int:
    digits = "".join(c for c in config if c.isdigit())
    first_and_last = f'{digits[0]}{digits[-1]}'
    return int(first_and_last)


if __name__ == '__main__':
    with open('puzzle.txt', 'r') as file:
        content = file.read().split('\n')
        number_generator: Generator[int, None, None] = (get_first_last_digits(calibration) for calibration in content)
        res = sum(number_generator)
        print(res)
