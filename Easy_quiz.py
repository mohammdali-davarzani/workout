from math import factorial

day_of_year, number = input().split()

count = 0
factor = factorial(int(day_of_year))
for i in str(factor):
    if i == number:
        count += 1

print(count)
