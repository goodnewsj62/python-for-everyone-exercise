
# 1.

def chop(list_):
    del list_[0]
    del list_[1:]
    return None

def middle(list_):
    del list_[1:-1]
    return list_


print(chop([1,2,34,5]))
print(middle([1,2,3,4]))

# 2. upgrading the code so if the list made from a line does not have an index
# of 2 we will display does not have an index of 2


fhand = open('./files/mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    try:
        print(words[2])
    except:
        print("does not have an index of two")


# 3.

fhand = open('./files/mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 or words[0] != 'From':
        continue
    try:
        print(words[2])
    except:
        print("does not have an index of two")

# 4.
hold_words = []
with open('./files/romeo.txt', 'rt') as file:
    for line in file:
        line = line.split()
        for word in line:
            print(word)
            if word in hold_words:
                continue
            hold_words.append(word)
hold_words.sort()
print(hold_words)

# 5.

count = 0
with open('./files/mbox-short.txt', 'rt') as file:
    for line in file:
        if line.startswith('From '):
            line = line.split()
            print(line[1])
            count += 1
    print("There were",count,"lines")

# 6.
inp = 0
hold = []
while inp != 'done':
    inp = input("Enter a number: ")

    if inp != 'done':
        try:
            inp = int(inp)
            hold.append(inp)
        except ValueError:
            print("invalid input")

print("The maximum number: ",max(hold))
print("The minimum number: ", min(hold))


