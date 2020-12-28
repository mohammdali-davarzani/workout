entry = input().split()

output = list()
for i in range(int(entry[0])):
    output.append("copy")
    output.append("of")

output.append(entry[1])

print(*output)
