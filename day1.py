with open('fuel.txt') as f:
    string_data = f.readlines()
    data = [int(i) for i in string_data]

count = 0
for number in data:
    count+= number//3 - 2
print(count)