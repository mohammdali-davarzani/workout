number = int(input())
words = input().split()

n = number
for i in range(number):
    print(words[n-1], end=' ')
    n -= 1