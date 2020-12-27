n = int(input())

firts_step = ["W","w", "!"]
for i in range(n):
    firts_step.insert(1, "o")

output = ""
print(output.join(firts_step))