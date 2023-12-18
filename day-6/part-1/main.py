import math


def filter_empty_strings_and_convert_to_numbers(data: list[str]) -> list[int]:
    data = list(filter(lambda x: x != '', data))
    data = list(map(lambda x: int(x), data))
    return data


def get_distance(speed: int, time: int):
    return speed * time


def get_race_possible_distance_outcomes(race) -> list[int]:
    all_race_outcomes = []
    for i in range(race['time'] + 1):
        speed = i
        time = race['time'] - i
        all_race_outcomes.append(get_distance(speed, time))
    print(all_race_outcomes)
    return all_race_outcomes


def main():
    with open('sample.txt') as file:
        contents = file.read().split("\n")
        times = contents[0].split(':')[1].strip().split(" ")
        distances = contents[1].split(':')[1].strip().split(" ")
        times = filter_empty_strings_and_convert_to_numbers(times)
        distances = filter_empty_strings_and_convert_to_numbers(distances)
        print(times)
        print(distances)
        assert len(times) == len(distances)

        races = []
        for race in zip(times, distances):
            races.append({'time': race[0], 'distance': race[1]})
        print(races)
        correct_plays_counters = []
        for race in races:
            t = get_race_possible_distance_outcomes(race)
            t = [d for d in t if d > race['distance']]
            correct_plays_counters.append(len(t))
        print(correct_plays_counters)
        print(math.prod(correct_plays_counters))


if __name__ == '__main__':
    main()
'''
0 7 0
1 6 6
2 5 10
3 4 12

'''