# 1.

hour_input = int(input("Enter hours: "))
rate_input = float(input("Enter Rate: "))

if hour_input > 40:
    rate_input *= 1.5

pay = hour_input * rate_input
print("Pay: ", pay)

# 2.
try:
    hour_input = int(input("Enter hours: "))
    rate_input = float(input("Enter Rate: "))
except ValueError:
    print("Error, please enter numeric input")
except:
    print("Invalid input ")

if hour_input > 40:
    rate_input *= 1.5

pay = hour_input * rate_input
print("Pay: ", pay)

# 3.
def enter_score():
    score_input = float(input("Enter a score between 0.0 to 1.0: "))

    if score_input < 0 or score_input > 1:
        print("Invalid Score")
        return  0
    if score_input >= 0.9:
        print("A")
    elif score_input >= 0.8:
        print("B")
    elif score_input >= 0.7:
        print("C")
    elif score_input >= 0.6:
        print("B")
    else:
        print("F")


enter_score()


