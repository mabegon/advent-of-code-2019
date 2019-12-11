SAN = "SAN"
YOU = "YOU"
COM = "COM"
FILEPATH = '../input.txt'


def compute_total_system_orbits(input_data: list) -> int:
    total_system_orbits = 0

    connections = get_connections(input_data)

    for orbit_object in connections.keys():
        total_system_orbits += orbits_to_com(connections, orbit_object)
    return total_system_orbits


def get_connections(input_data):
    connections = dict({})
    for orbital_connection in input_data:
        central_object, orbit_object = orbital_connection.split(")")
        connections.update({orbit_object: central_object})
    return connections


def orbits_to_com(connections, orbit_object):
    total = forward_orbits_between_two_objects(connections, orbit_object, COM)
    return total


def forward_orbits_between_two_objects(connections: dict, from_object: str, to_object: str) -> int:
    central_object = ""
    sub_total: int = 0

    while central_object != to_object:
        central_object = connections.get(from_object)
        from_object = central_object
        sub_total += 1
    return sub_total


def compute_orbits_between_you_and_san(input_data: list):

    connections = get_connections(input_data)

    you_path = orbits_path_to_com(connections, YOU)
    san_path = orbits_path_to_com(connections, SAN)

    intersection = set(you_path) & set(san_path)
    intersection.remove(COM)

    if len(intersection) == 0:
        return 0

    you_distances = []
    san_distances = []
    for i in intersection:
        you_distances.append(forward_orbits_between_two_objects(connections, YOU, i)-1)
        san_distances.append(forward_orbits_between_two_objects(connections, SAN, i)-1)
    you_distances.sort()
    san_distances.sort()

    return you_distances[0] + san_distances[0]


def orbits_path_to_com(connections, from_object):
    central_object = ""
    you_path = set()
    while central_object != COM:
        central_object = connections.get(from_object)
        from_object = central_object
        you_path.add(central_object)
    return you_path


def main():
    input_data = []
    with open(FILEPATH) as fp:
        for line in fp:
            input_data.append(line.strip())
    total_system_orbits = compute_total_system_orbits(input_data)
    print(str.format("The answer of part 1 is : {}", total_system_orbits))

    total_to_santa = compute_orbits_between_you_and_san(input_data)
    print(str.format("The answer of part 2 is : {}", total_to_santa))


if __name__ == '__main__':
    main()