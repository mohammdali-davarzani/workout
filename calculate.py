import statistics 

numbers = list()

for i in range(4):
    numbers.append(int(input()))

multiple = 1
for i in numbers:
    multiple = i * multiple

print("Sum : {:.6f}".format(sum(numbers)))
print("Average : {:.6f}".format(statistics.mean(numbers)))
print("Product : {:.6f}".format(multiple))
print("MAX : {:.6f}".format(max(numbers)))
print("MIN : {:.6f}".format(min(numbers)))