from pydantic import BaseModel


class Map(BaseModel):
    destination_range_start: int
    source_range_start: int
    range_length: int


def parsing(data):
    data = [row for row in data if row]

    seeds = data[0]
    seeds = seeds.split(":")[1].split()
    seeds = [int(x) for x in seeds]

    maps = {}
    maps_counter = 0
    for row in data[1:]:
        row = row.split(":")

        if len(row) == 2:
            maps |= {maps_counter: []}
            maps_counter += 1
        else:
            row = row[0].split()
            drs = int(row[0])
            srs = int(row[1])
            rl = int(row[2])

            map_ = Map(
                destination_range_start=drs,
                source_range_start=srs,
                range_length=rl,
            )
            maps[maps_counter - 1].append(map_)

    return seeds, maps


def part_1(data):
    seeds, maps = parsing(data)

    locations = []
    for seed in seeds:
        for _, map_list in maps.items():
            for map_ in map_list:
                if map_.source_range_start <= seed < map_.source_range_start + map_.range_length:
                    diff = seed - map_.source_range_start
                    seed = map_.destination_range_start + diff
                    break
        locations.append(seed)

    return min(locations)


class SeedIntervals(BaseModel):
    start: int
    end: int
    transformed: bool = False


def part_2(data):
    seeds, maps = parsing(data)

    seeds_start = seeds[::2]
    seeds_range = seeds[1::2]

    location = None

    seeds_intervals = []
    end_intervals = []
    for i in range(len(seeds_start)):
        start_seed = seeds_start[i]
        end_seed = seeds_start[i] + seeds_range[i] - 1

        seeds_intervals.append(SeedIntervals(start=start_seed, end=end_seed))

    for interval in seeds_intervals:
        working_intervals = [interval]

        for _, map_list in maps.items():
            working_intervals = [
                SeedIntervals(start=x.start, end=x.end, transformed=False)
                for x in working_intervals
            ]

            for map_ in map_list:
                working_intervals = evaluate_intervals(intervals=working_intervals, map_=map_)
        end_intervals.extend(working_intervals)

    location = None
    for interval in end_intervals:
        if location is None or interval.start < location:
            location = interval.start
    return location


def evaluate_intervals(intervals, map_):
    new_intervals = []
    for interval in intervals:
        if interval.transformed is False:
            if interval.end < map_.source_range_start:
                new_intervals.append(
                    SeedIntervals(start=interval.start, end=interval.end, transformed=False)
                )
            elif interval.start >= map_.source_range_start + map_.range_length:
                new_intervals.append(
                    SeedIntervals(start=interval.start, end=interval.end, transformed=False)
                )
            elif interval.start >= map_.source_range_start:
                if interval.end < map_.source_range_start + map_.range_length:
                    start = interval.start + map_.destination_range_start - map_.source_range_start
                    end = interval.end + map_.destination_range_start - map_.source_range_start
                    new_intervals.append(SeedIntervals(start=start, end=end, transformed=True))
                else:
                    interval1 = SeedIntervals(
                        start=interval.start
                        + map_.destination_range_start
                        - map_.source_range_start,
                        end=map_.destination_range_start + map_.range_length - 1,
                        transformed=True,
                    )
                    interval2 = SeedIntervals(
                        start=map_.source_range_start + map_.range_length,
                        end=interval.end,
                        transformed=False,
                    )
                    new_intervals.extend([interval1, interval2])
            elif interval.end < map_.source_range_start + map_.range_length:
                interval1 = SeedIntervals(
                    start=interval.start,
                    end=map_.source_range_start - 1,
                    transformed=False,
                )
                interval2 = SeedIntervals(
                    start=map_.destination_range_start,
                    end=interval.end + map_.destination_range_start - map_.source_range_start,
                    transformed=True,
                )
                new_intervals.extend([interval1, interval2])
            else:
                interval1 = SeedIntervals(
                    start=interval.start,
                    end=map_.source_range_start - 1,
                    transformed=False,
                )
                interval2 = SeedIntervals(
                    start=map_.source_range_start
                    + map_.destination_range_start
                    - map_.source_range_start,
                    end=map_.destination_range_start + map_.range_length - 1,
                    transformed=True,
                )
                interval3 = SeedIntervals(
                    start=map_.source_range_start + map_.range_length,
                    end=interval.end,
                    transformed=False,
                )
                new_intervals.extend([interval1, interval2, interval3])
        else:
            new_intervals.append(interval)

    return new_intervals
