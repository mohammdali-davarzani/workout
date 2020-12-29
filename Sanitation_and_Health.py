score = int(input())
travel_days = int(input())

if (travel_days == 0):
    print(20)

elif (travel_days == 7):
    print(score)

else:
    output = score - travel_days
    if (output < 0):
        print(0)
    else:
        print(output)