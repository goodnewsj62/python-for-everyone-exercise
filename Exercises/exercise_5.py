# 1.


total = 0
count = 0
inp = 0
while inp != 'done':
    inp = input("Enter a number: ")

    if inp != 'done':
        try:
            inp = int(inp)
            total += inp
            count += 1
        except ValueError:
            print("invalid input")


average = total/count
print("Total: ",total)
print("Average: ",average)

# 2.
inp = 0
count = 0
hold_max = 0
hold_min = 0

while inp != 'done':
    inp = input("Enter a number: ")

    if inp != 'done':
        try:
            inp = int(inp)

            if count == 0:
                hold_min = inp
            if inp > hold_max:
                hold_max = inp
            if inp < hold_min:
                hold_min = inp

            count += 1

        except ValueError:
            print("invalid input")

print("The maximum number: ",hold_max )
print("The minimum number: ", hold_min )