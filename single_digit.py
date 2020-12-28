n = input()

first = list()
for i in n:
    first.append(int(i))

output = 0
while len(first) > 1:
    output = sum(first)

print(output) 