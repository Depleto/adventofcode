def input_code_generator(input_txt):
    with open(input_txt) as t:
        read = t.read()
        string_list = read.split(',')
        for i in range(len(string_list)):
            string_list[i] = int(string_list[i])
        return string_list


def parameter_add(data, i):
    string_value = str(data[i])
    parameter_value = string_value[:-2]
    # v1_0 = data[data[i+1]]
    # v2_0 = data[data[i+2]]
    # v1_1 = data[i+1]
    # v2_1 = data[i+2]

    if parameter_value == '00' or parameter_value == '0':
        v1_0 = data[data[i + 1]]
        v2_0 = data[data[i + 2]]
        data[data[i + 3]] = v1_0 + v2_0

    elif parameter_value == '10':
        v1_0 = data[data[i + 1]]
        v2_1 = data[i + 2]
        data[data[i + 3]] = v1_0 + v2_1

    elif parameter_value == '01' or parameter_value == '1':
        v1_1 = data[i + 1]
        v2_0 = data[data[i + 2]]
        data[data[i + 3]] = v1_1 + v2_0

    else:
        v1_1 = data[i + 1]
        v2_1 = data[i + 2]
        data[data[i + 3]] = v1_1 + v2_1

    return data


def parameter_multiply(data, i):
    string_value = str(data[i])
    parameter_value = string_value[:-2]

    # v1_0 = data[data[i+1]]
    # v2_0 = data[data[i+2]]
    # v1_1 = data[i+1]
    # v2_1 = data[i+2]
    if parameter_value == '00' or parameter_value == '0':
        v1_0 = data[data[i + 1]]
        v2_0 = data[data[i + 2]]
        data[data[i + 3]] = v1_0 * v2_0

    elif parameter_value == '10':
        v1_0 = data[data[i + 1]]
        v2_1 = data[i + 2]
        data[data[i + 3]] = v1_0 * v2_1

    elif parameter_value == '01' or parameter_value == '1':
        v1_1 = data[i + 1]
        v2_0 = data[data[i + 2]]
        data[data[i + 3]] = v1_1 * v2_0

    else:
        v1_1 = data[i + 1]
        v2_1 = data[i + 2]
        data[data[i + 3]] = v1_1 * v2_1

    return data


def parameter_output(data, i):
    string_value = str(data[i])
    parameter_value = string_value[:-2]
    if parameter_value == '1':
        print(data[i + 1])
    else:
        print(data[data[i + 1]])


def parameter_jumpiftrue(data, i):
    string_value = str(data[i])
    parameter_value = string_value[:-2]
    if parameter_value == '00' or parameter_value == '0' or len(string_value) == 1:
        if data[data[i + 1]] != 0:
            new_index = data[data[i + 2]]
            return new_index
        else:
            return i + 3

    elif parameter_value == '10':
        if data[data[i + 1]] != 0:
            new_index = data[i + 2]
            return new_index
        else:
            return (i + 3)

    elif parameter_value == '01' or parameter_value == '1':
        if data[i + 1] != 0:
            new_index = data[data[i + 2]]
            return new_index
        else:
            return (i + 3)

    else:  # '11'
        if data[i + 1] != 0:
            new_index = data[i + 2]
            return new_index
        else:
            return (i + 3)


def jumpiffalse(data, i):
    string_value = str(data[i])
    parameter_value = string_value[:-2]
    if parameter_value == '00' or parameter_value == '0' or len(string_value) == 1:
        if data[data[i + 1]] == 0:
            new_index = data[data[i + 2]]
            return new_index
        else:
            return (i + 3)

    elif parameter_value == '10':
        if data[data[i + 1]] == 0:
            new_index = data[i + 2]
            return new_index
        else:
            return (i + 3)

    elif parameter_value == '01' or parameter_value == '1':
        if data[i + 1] == 0:
            new_index = data[data[i + 2]]
            return new_index
        else:
            return (i + 3)

    else:  # '11'
        if data[i + 1] == 0:
            new_index = data[i + 2]
            return new_index
        else:
            return (i + 3)


def lessthan(data, i):
    string_value = str(data[i])
    parameter_value = string_value[:-2]
    if parameter_value == '00' or parameter_value == '0' or len(string_value) == 1:
        if data[data[i + 1]] < data[data[i + 2]]:
            data[data[i + 3]] = 1
        else:
            data[data[i + 3]] = 0

    elif parameter_value == '10':
        if data[data[i + 1]] < data[i + 2]:
            data[data[i + 3]] = 1
        else:
            data[data[i + 3]] = 0

    elif parameter_value == '01' or parameter_value == '1':
        if data[i + 1] < data[data[i + 2]]:
            data[data[i + 3]] = 1
        else:
            data[data[i + 3]] = 0

    else:  # 1,1
        if data[i + 1] < data[i + 2]:
            data[data[i + 3]] = 1
        else:
            data[data[i + 3]] = 0

    return data


def equalsto(data, i):
    string_value = str(data[i])
    parameter_value = string_value[:-2]
    if parameter_value == '00' or parameter_value == '0' or len(string_value) == 1:
        if data[data[i + 1]] == data[data[i + 2]]:
            data[data[i + 3]] = 1
        else:
            data[data[i + 3]] = 0

    elif parameter_value == '10':
        if data[data[i + 1]] == data[i + 2]:
            data[data[i + 3]] = 1
        else:
            data[data[i + 3]] = 0

    elif parameter_value == '01' or parameter_value == '1':
        if data[i + 1] == data[data[i + 2]]:
            data[data[i + 3]] = 1
        else:
            data[data[i + 3]] = 0

    else:  # 1,1
        if data[i + 1] == data[i + 2]:
            data[data[i + 3]] = 1
        else:
            data[data[i + 3]] = 0

    return data


def placeholder():
    string_value = str(data[i])
    parameter_value = string_value[:-2]
    if parameter_value == '00' or parameter_value == '0' or len(string_value) == 1:
        pass

    elif parameter_value == '10':
        pass

    elif parameter_value == '01' or parameter_value == '1':
        pass

    else:  # 1,1
        pass

    return data


def intcode_computer_3(data):
    i = 0
    while i in range(len(data)):

        if data[i] == 3:
            input_value = int(input("Please provide a number: "))
            data[data[i + 1]] = input_value
            i += 2

        elif data[i] == 1:
            data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
            i += 4

        elif data[i] == 2:
            data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
            i += 4


        elif data[i] == 99:
            print("Program Stopped")
            return i



        else:
            string_value = str(data[i])
            opcode = string_value[-1]
            if opcode == '1':
                data = parameter_add(data, i)
                i += 4

            elif opcode == '4':
                parameter_output(data, i)
                i += 2

            elif opcode == '5':
                i = parameter_jumpiftrue(data, i)

            elif opcode == '6':
                i = jumpiffalse(data, i)

            elif opcode == '7':
                data = lessthan(data, i)
                i += 4

            elif opcode == '8':
                equalsto(data, i)
                i += 4


            else:
                data = parameter_multiply(data, i)
                i += 4


if __name__ == "__main__":
    data = input_code_generator('day5.txt')
    print(data)
    print(data[46:])
    intcode_computer_3(data)
