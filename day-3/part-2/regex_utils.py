import re
from typing import Match


def get_asterisks_matches(input_string: str) -> list[Match]:
    pattern = re.compile(r'\*')
    matches = []
    start_pos = 0
    while True:
        match = pattern.search(input_string, start_pos)
        if not match:
            break
        matches.append(match)
        start_pos = match.end()
    return matches
