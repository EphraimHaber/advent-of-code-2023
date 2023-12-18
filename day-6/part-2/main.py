def get_distance(speed: int, time: int):
    return speed * time


def binary_search_for_last_number_to_not_win(distance_to_beat: int, total_race_time: int):
    start, end = 0, total_race_time
    while start <= end:
        mid = (start + end) // 2
        if get_distance(mid, total_race_time - mid) >= distance_to_beat:
            start = mid + 1
        else:
            end = mid - 1
    return start - 1


if __name__ == '__main__':
    with open('puzzle.txt') as file:
        data = file.read().split("\n")
        total_time = int("".join(c for c in data[0] if c.isnumeric()))
        distance = int("".join(c for c in data[1] if c.isnumeric()))

        last_value_to_uphold = binary_search_for_last_number_to_not_win(distance, total_time)
        first_value_to_uphold = total_time - last_value_to_uphold

        if last_value_to_uphold == -1:
            print("Record unbreakable")
            exit(0)
        if first_value_to_uphold == last_value_to_uphold:
            print("only one")
            exit(0)

        t = last_value_to_uphold - first_value_to_uphold + 1
        pairs = t if t % 2 == 0 else t - 1
        print(pairs)  # 34788142


