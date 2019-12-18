with open('fuel.txt') as f:
    string_data = f.readlines()
    data = [int(i) for i in string_data]

count = 0
for number in data:
    i = number
    while i//3 >2:
        count += i//3 - 2
        i = i//3 - 2
print(count)