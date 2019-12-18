def adjacent_digits(num):
    string_num = str(num)
    for i in range(5):
        if string_num[i] == string_num[i+1]:
            return True
def increasing_or_same(num):
    string_num = str(num)
    for i in range(5):
        if int(string_num[i+1]) < int(string_num[i]):
            return False
    return True

def only_two_adjacent(num):
    string_num = str(num)
    for i in range(5):
        if string_num[i] == string_num[i+1] and string_num.count(string_num[i])==2:
            return True


def number_of_passwords():
    passwords = 0
    for i in range(235741,706949):
        if increasing_or_same(i) and adjacent_digits(i):
            passwords +=1
    print(passwords)
    return passwords

def number_of_passwords_part2():
    passwords = 0
    for i in range(235741,706949):
        if increasing_or_same(i) and adjacent_digits(i) and only_two_adjacent(i):
            passwords +=1
    print(passwords)
    return passwords


if __name__ == "__main__":
    number_of_passwords()
    number_of_passwords_part2()