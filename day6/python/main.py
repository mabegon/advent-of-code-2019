COM = "COM"
FILEPATH = '../input.txt'

def compute_total_system_orbits(input_data: list) -> int:

    total_system_orbits = 0
    connections = dict({})

    for orbital_connection in input_data:
        central_object, orbit_object = orbital_connection.split(")")
        connections.update({orbit_object: central_object})

    for orbit_object in connections.keys():
        total_system_orbits += orbits_to_com(connections, orbit_object)
    return total_system_orbits


def orbits_to_com(connections, orbit_object):
    central_object = ""
    sub_total = 0
    while central_object != COM:
        central_object = connections.get(orbit_object)
        orbit_object = central_object
        sub_total += 1

    return sub_total


def main():
    input_data = []
    with open(FILEPATH) as fp:
        for line in fp:
            input_data.append(line.strip())
    total_system_orbits = compute_total_system_orbits(input_data)
    print(str.format("The answer of part 1 is : {}", total_system_orbits))


if __name__ == '__main__':
    main()