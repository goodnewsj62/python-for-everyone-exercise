# 1.

import re

user_input = input("Enter the regular expression: ")

count = 0

with open('./files/mbox-short.txt', 'rt') as file:
    for line in file:
        line = line.rstrip()
        hold = re.findall(user_input, line)
        for each in hold:
            count += 1

print('There are ',count,' lines that match ',user_input)


inp = input("Enter the file name (mbox-short.txt): ")
file_name = r'./files/' + inp


count = 0
total = 0
try:
    with open('./files/mbox-short.txt', 'rt') as file:
        for line in file:
            line = line.rstrip()
            hold = re.findall('^N.+: ([0-9]+)',line)
            for each in hold:
                total += float(each)
                count += 1
except:
    print('enter mbox-short.txt')


average = total/count
print('The average of the numbers equals: ', average)

