def preprocessing(data):
    data = [row.split() for row in data]
    valves = {}
    for row in data:
        v_id = row[1]
        rate = int(row[4].split("=")[1].strip(";"))
        possible_valves = [x.strip(",") for x in row[9:]]
        valves[v_id] = {"rate": rate, "possible_valves": possible_valves}

    for v_id in valves:
        find_dists(valves, v_id)

    return valves


def find_dists(valves, v_id):
    valves[v_id]["distances"] = {}
    possible_valves = valves[v_id]["possible_valves"]
    dist = 0
    while possible_valves:
        ids = possible_valves
        possible_valves = []
        dist += 1
        for current_id in ids:
            if current_id in valves[v_id]["distances"]:
                continue
            valves[v_id]["distances"][current_id] = dist
            possible_valves.extend(valves[current_id]["possible_valves"])


def find_max_flow(valves, v_id, visited, time, rate):
    max_flow = (30 - time) * rate
    cur_valve = valves[v_id]

    for pos_valve_id, dist in cur_valve["distances"].items():
        if pos_valve_id == v_id or pos_valve_id in visited:
            continue

        pos_valve_rate = valves[pos_valve_id]["rate"]
        time_increment = dist + 1

        if pos_valve_rate == 0 or time + time_increment >= 30:
            continue
        visited.add(pos_valve_id)

        max_flow = max(
            max_flow,
            rate * time_increment
            + find_max_flow(
                valves,
                pos_valve_id,
                visited,
                time + time_increment,
                rate + pos_valve_rate,
            ),
        )

        visited.remove(pos_valve_id)

    return max_flow


def part_1(data):
    valves = preprocessing(data)

    start_valve = "AA"
    visited = set()
    start_time = 0
    start_rate = 0
    return find_max_flow(valves, start_valve, visited, start_time, start_rate)


def find_max_flow_part2(valves, my_v_id, my_time, el_v_id, el_time, visited, time, rate):
    if time == 26:
        return 0
    if my_time > 0 and el_time > 0:
        time_increment = min(my_time, el_time)
        new_rate = rate
        if my_time == time_increment:
            new_rate += valves[my_v_id]["rate"]
        if el_time == time_increment:
            new_rate += valves[el_v_id]["rate"]

        return rate * time_increment + find_max_flow_part2(
            valves,
            my_v_id,
            my_time - time_increment,
            el_v_id,
            el_time - time_increment,
            visited,
            time + time_increment,
            new_rate,
        )

    mover, cur_valve_id = ("me", my_v_id) if my_time == 0 else ("el", el_v_id)

    cur_valve = valves[cur_valve_id]
    max_flow = 0

    for pos_valve_id, dist in cur_valve["distances"].items():
        if pos_valve_id == cur_valve_id or pos_valve_id in visited:
            continue

        pos_valve_rate = valves[pos_valve_id]["rate"]
        time_increment = dist + 1

        if pos_valve_rate == 0 or time + time_increment >= 26:
            continue
        visited.add(pos_valve_id)

        max_flow = max(
            max_flow,
            find_max_flow_part2(
                valves,
                pos_valve_id if mover == "me" else my_v_id,
                time_increment if mover == "me" else my_time,
                pos_valve_id if mover == "el" else el_v_id,
                time_increment if mover == "el" else el_time,
                visited,
                time,
                rate,
            ),
        )
        visited.remove(pos_valve_id)

    time_increment = 26 - time
    max_flow = max(
        max_flow,
        find_max_flow_part2(
            valves,
            pos_valve_id if mover == "me" else my_v_id,
            time_increment if mover == "me" else my_time,
            pos_valve_id if mover == "el" else el_v_id,
            time_increment if mover == "el" else el_time,
            visited,
            time,
            rate,
        ),
    )

    return max_flow


def part_2(data):
    valves = preprocessing(data)

    start_valve = "AA"
    visited = set()
    start_time = 0
    start_rate = 0
    return find_max_flow_part2(
        valves,
        start_valve,
        start_time,
        start_valve,
        start_time,
        visited,
        start_time,
        start_rate,
    )
