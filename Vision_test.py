number = int(input())
main_word = input()
input_word = input()

count = 0
for i in range(number):
    if (main_word[i] != input_word[i]):
        count += 1

print(count)