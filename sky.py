number_1, number_2 = input().split()

count = 0
for i in range(int(number_1)):
    string = input()
    for j in range(int(number_2)):
        if (string[j] == "*"):
            count += 1

print(count)