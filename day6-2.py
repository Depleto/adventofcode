with open('orbits.txt') as f:
    file = f.read()
    text_list = file.split('\n')
def direct_path(input_list,orb):
    direct_path = orb
    while orb[-1] != "COM":

        for i in text_list:
            if i[-3:] == orb[0]:
                direct_path.append(i[:3])
                orb[0] = i[:3]
                break
    return direct_path

you_list = (direct_path(text_list,["YOU"]))
san_list = (direct_path(text_list,["SAN"]))

you_list[0] = "YOU"
san_list[0] = "SAN"

common = [i for i in you_list if i in san_list]

stepsA = you_list.index(common[0]) - 1
stepsB = san_list.index(common[0]) - 1

print(stepsA+stepsB)
