def get_seeds(seed_line: str) -> list[int]:
    seed_line = seed_line.split(':')[1].split('\n')[0].split(" ")[1:]
    seed_line = [int(seed) for seed in seed_line]
    return seed_line


def main():
    with open('puzzle.txt', 'r') as file:
        content = file.read()
        content_lines = content.split('\n')+['']
        seeds = get_seeds(content.split('\n')[0])
        # print(sum(seeds))
        # seed_ranges: list[range] = []
        # seed_ranges.append(range(79, 79 + 14))

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
        for curr_seed in seeds:
            # path = f'{curr_seed}'
            for key in maps_keys:
                # is_found = False
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
    print(min(final_destinations))


if __name__ == '__main__':
    main()
