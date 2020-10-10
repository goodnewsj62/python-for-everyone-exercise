
# 1.
user_inp = input("Enter your name: ")
print("Hello",user_inp)

# 2.
hour_input = input("Enter hours: ")
rate_input = input("Enter Rate: ")

pay = int(hour_input) * float(rate_input)
print("Pay: ", pay)

# 3.
width = 17
height = 12.0

# width//2  equals 8
# width/2 equals 8.5
# height/2 equals 6
# 1 + 2 * 5 equals 11


# 4.

print("---------------Covert Temperature From Celsius To Fahrenheit-------------")
temp_input = input("Enter temperature")
fah_temp = float(temp_input) * 1.8 + 32

print("The temperature in fahrenheit is: " ,fah_temp)
