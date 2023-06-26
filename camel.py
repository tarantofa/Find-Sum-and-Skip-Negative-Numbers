posSum = 0

print("Please Enter 10 Numbersto Find Positive Sum\n")
for i in range(1, 11):
    num = int(input("Number %d = " %i))

    if num < 0:
        continue

    posSum = posSum + num

print("The Sum of 10 Numbers by Skipping Negative Numbers = ", posSum)
