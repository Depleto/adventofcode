with open('orbits.txt') as f:
    file = f.read()
    text_list = file.split('\n')

for i in text_list:
    if i[:3] == "COM":
        print(i)


def orbit_map(input_list):
    total_orbits = 1
    orbit_counter = 2
    previous_planet = ['7ZS']
    next_planet = []

    while True:
        for i in input_list:
            if i[:3] in previous_planet:
                total_orbits += orbit_counter
                next_planet.append(i[-3:])

        if next_planet == []:
            break
        previous_planet = next_planet
        next_planet = []
        orbit_counter += 1

    print(total_orbits)


orbit_map(text_list)

