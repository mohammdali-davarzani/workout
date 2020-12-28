numbers = input().split()

total = 0
n = 2
while n > 0:
    if numbers[n] == "0":
        numbers.remove(numbers[n])
    n -= 1


if len(numbers) == 3:
    for i in numbers:
        if int(i) > 0:
            total = total + int(i)

if total == 180:
    print("Yes")

else:
    print("No")