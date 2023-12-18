import random
from datetime import datetime


chance_of_event = 1 / 10000


def get_seeds(seed_line: str) -> list[int]:
    seed_line = seed_line.split(':')[1].split('\n')[0].split(" ")[1:]
    seed_line = [int(seed) for seed in seed_line]
    return seed_line


def main():
    with open('puzzle.txt', 'r') as file:
        content = file.read()
        content_lines = content.split('\n')+['']
        seeds = get_seeds(content.split('\n')[0])
        seed_ranges: list[range] = []
        # seed_ranges.append(range(79, 79 + 14))
        # print(list(seed_ranges[0]))
        # for curr_seed_range in seed_ranges:
        #     for curr_seed in curr_seed_range:
        #         print(curr_seed)
        for i in range(0, len(seeds), 2):
            seed_ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))
        map_start_locations = []
        for i, line in enumerate(content.split("\n")):
            line: str = line
            if 'map' in line:
                map_start_locations.append(i)
        maps = {}
        for title_index in map_start_locations:
            maps[content_lines[title_index]] = []
        maps_keys = list(maps.keys())
        map_start_locations = [element + 1 for element in map_start_locations]
        map_start_locations.append(len(content_lines) - 1)
        for i in range(len(map_start_locations) - 1):
            for info_line_index in range(map_start_locations[i], map_start_locations[i+1]):
                if not content_lines[info_line_index].strip():
                    continue
                if content_lines[info_line_index][0].isalpha():
                    continue
                if content_lines[info_line_index].strip():
                    temp_mapping = [int(num)for num in content_lines[info_line_index].split(" ")]
                    maps[maps_keys[i]].append(temp_mapping)
        final_destinations = []
        for curr_seed_range in seed_ranges:
            for curr_seed in curr_seed_range:
                curr_step = curr_seed
                # path = f'{curr_seed}'
                for key in maps_keys:
                    is_found = False
                    for map_range in maps[key]:
                        source_start = map_range[1]
                        range_length = map_range[2]
                        dest_start = map_range[0]
                        if curr_seed in range(source_start, source_start + range_length):
                            # path += f'->{dest_start + curr_seed - source_start}'
                            curr_seed = dest_start + curr_seed - source_start
                            # is_found = True
                            break
                    # if not is_found:
                        # path += f'->{curr_seed}'

                # print(path)
                final_destinations.append(curr_seed)
                # print("curr_seed", curr_seed/)
                random_number = random.random()
                if random_number < chance_of_event:
                    # number = 3.141592653589793
                    #
                    # # Format the number to show 5 decimal points
                    # formatted_number = "{:.5f}".format(number)
                    #
                    # print(formatted_number)
                    number = curr_step / curr_seed_range.stop
                    formatted_number = "{:.5f}".format(number)
                    print(f'{formatted_number}% - {datetime.now().strftime("%H:%M:%S")} - {curr_step}-{curr_seed_range}')
            print(curr_seed_range)
            break
    print(min(final_destinations))


if __name__ == '__main__':
    main()
