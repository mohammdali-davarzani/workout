condition = input()

green = 0
yellow = 0
red = 0
count = 0

for i in condition:
    if (i == "G"):
        green += 1
    elif (i == "Y"):
        yellow += 1
    elif (i == "R"):
        red += 1

if (red >= 3) or  ((red >= 2) and (yellow >= 2)) or (red == 5 and green == 0 and yellow == 0) or (red == 0 and green == 0 and yellow == 5):
    count += 1

if (count >= 1):
    print("nakhor lite")
else:
    print("rahat baash")