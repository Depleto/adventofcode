with open('wire.txt') as w:
    read = w.read()

    input_list = read.split()
    input1 = input_list[0].split(',')
    input2 = input_list[1].split(',')

def wire_path(wire):
    wire1_path = []
    x=0
    y=0
    for i in wire:
        direction = i[0]
        move = int(i[1:])


        if direction == "D":
            for i in range(1, move + 1):
                wire1_path.append((x, y))
                y -= 1
        elif direction == "U":
            for i in range(1, move + 1):
                wire1_path.append((x, y))
                y += 1
        elif direction == "L":
            for i in range(1, move + 1):
                wire1_path.append((x, y))
                x -= 1
        elif direction == "R":
            for i in range(1, move + 1):
                wire1_path.append((x, y))
                x += 1
    return wire1_path


def manhattan_distance(input1,input2):
    path1 = set(wire_path(input1))
    path2 = set(wire_path(input2))
    intersects = path1.intersection(path2)
    sums = [abs(a) + abs(b) for a, b in intersects]
    sums.sort()
    print(sums[1])

def combined_steps(input1,input2):
    path1_set = set(wire_path(input1))
    path2_set = set(wire_path(input2))
    intersects = path1_set.intersection(path2_set)

    path1 = wire_path(input1)
    path2 = wire_path(input2)

    total_steps = []

    for i in intersects:
        steps1 = path1.index(i)
        steps2 = path2.index(i)
        total_steps.append(steps1+steps2)

    total_steps.sort()
    print(total_steps)



    #total_steps = [a+b for a,b in zip(steps1,steps2)]
    #total_steps.sort()
    #print(total_steps[1])




if __name__ == "__main__":
    combined_steps(input1,input2)









