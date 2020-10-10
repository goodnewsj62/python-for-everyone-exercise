import random

# 1.

for n in range(10):
    print(random.random())

# 2.
# repeat_lyrics()
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# 3.
# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print('I sleep all night and I work all day.')
# repeat_lyrics()

# 4. It indicates the start of a function

# 5.
def fred():
    print("Zap")
def jane():
    print("ABC")

jane() # ABC
fred()# Zap
jane()# ABC

# 6.

def compute_pay(hour_input, rate_input):
    if hour_input > 40:
        rate_input *= 1.5

    return hour_input * rate_input

print(compute_pay(45,1))

def compute_grade(score_input):
    if score_input < 0 or score_input > 1:
        print("Invalid Score")
        return  0
    if score_input >= 0.9:
        return "A"
    elif score_input >= 0.8:
       return "B"
    elif score_input >= 0.7:
        return "C"
    elif score_input >= 0.6:
        return "D"
    else:
        return "F"

print(compute_grade(1))

