from typing import Generator
from spelled_numbers import SPELLED_NUMBERS


def get_first_last_digits(config: str) -> int:
    first = len(config)
    last = -1
    first_key = ""
    last_key = ""
    for spelled_number in SPELLED_NUMBERS:
        if spelled_number in config:
            if config.find(spelled_number) < first:
                first = config.find(spelled_number)
                first_key = spelled_number
            if config.rfind(spelled_number) > last:
                last = config.rfind(spelled_number)
                last_key = spelled_number
    return int(f'{SPELLED_NUMBERS[first_key]}{SPELLED_NUMBERS[last_key]}')


if __name__ == '__main__':
    x = 1
    with open('puzzle.txt', 'r') as file:
        content = file.read().split('\n')
        number_generator: Generator[int, None, None] = (get_first_last_digits(calibration) for calibration in content)
        res = sum(number_generator)
        print(res)
