weight = float(input())
height = float(input())

bmi = weight / (height * height)

print("{:.2f}".format(bmi))

if (bmi < 18.5):
    print("Underweight")

elif (18.5 <= bmi < 25):
    print("Normal")

elif (25 <= bmi < 30):
    print("Overweight")

elif (bmi >= 30):
    print("Obese")

