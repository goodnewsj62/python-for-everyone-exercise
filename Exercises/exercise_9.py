# 1. a program that read words from a file and
# checks if word is in dictionary and give it any value or a
# constant value

dictionary_of_words = dict()

with open(r'./files/romeo.txt','rt') as file:
     hold = file.readlines()
     index = 0
     while index < len(hold):
         words = hold[index].strip('\n').split()
         for word in words:
                dictionary_of_words[word] = dictionary_of_words.get(word,0)
         index += 1

print(dictionary_of_words)

# 2.

day_count = dict()
with open(r'./files/mbox-short.txt', 'rt') as file:
    for line in file:
        if line.startswith("From"):
            line = line.strip().split()
            if len(line) > 3:
                day_count[line[2]] = day_count.get(line[2], 0) + 1

print(day_count)

# 3.

message_count = dict()
with open(r'./files/mbox-short.txt', 'rt') as file:
    for line in file:
        if line.startswith("From"):
            line = line.strip().split()
            if len(line) > 3:
                message_count[line[1]] = message_count.get(line[1], 0) + 1


print(message_count)

# 4.
max_ = 0
max_email = ''
for key,value in message_count.items():
    if value > max_:
        max_ = value
        max_email = key

print("The maximum messages was sent by: " ,max_email," ",max_)

# 5.

message_count = dict()
with open(r'./files/mbox-short.txt', 'rt') as file:
    for line in file:
        if line.startswith("From"):
            line = line.strip().split()
            if len(line) > 3:
                index = line[1].find('.')
                key = line[1][index + 1 : ]
                message_count[key] = message_count.get(key, 0) + 1

print(message_count)