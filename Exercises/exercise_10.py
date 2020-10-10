# 1.
message_count = dict()
with open(r'./files/mbox-short.txt', 'rt') as file:
    for line in file:
        if line.startswith("From"):
            line = line.strip().split()
            if len(line) > 3:
                message_count[line[1]] = message_count.get(line[1], 0) + 1

list_ = list()
for key,value in message_count.items():
    list_.append((value,key))


list_.sort()

print("The maximum is: ", list_[-1][1], list_[-1][0])

# 2.
hour_count = dict()
with open(r'./files/mbox-short.txt', 'rt') as file:
    for line in file:
        if line.startswith("From"):
            line = line.strip().split()
            if len(line) > 3:
                index = line[-2].find(':')
                key = line[-2][ : index]
                hour_count[key] = hour_count.get(key, 0) + 1

hour_list = list()

for key,value in hour_count.items():
    hour_list.append((value, key))

hour_list.sort()

for each in hour_list:
    print(each[1]," ",each[0])


# 3.

import string
letter_count = dict()
with open(r'./files/mbox-short.txt', 'rt') as file:
    for line in file:
        #removes punctuations special characters and numbers
            line = line.translate(str.maketrans('','', string.punctuation))
            line = line.translate(str.maketrans('','','1234567890@#$%^&*()_-+=|][{}\/>< '))
            line = line.lower()
            line = line.strip("\n").split()
            for letters in line:

                letters = letters.split()
                str_ = ''.join(letters)
                for letter in range(len(str_)):
                    letter_count[str_[letter]] = letter_count.get(str_[letter], 0) + 1


list_letter = []

for key,value in letter_count.items():
    list_letter.append((value,key))

list_letter.sort()

print('\n\nletters and how many times they appear\n\n')
for n in range(len(list_letter)):
    print(list_letter[n][1],list_letter[n][0])