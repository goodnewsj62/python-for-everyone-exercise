
#1. a program that read through a file and print line by line all in uppercase

with open('./files/words.txt', 'rt') as file:
    for line in file:
        line = line.strip().upper()
        print(line)

total = 0
count = 0
with open('./files/mbox-short.txt','rt') as file:
    for line in file:
        if line.startswith('X-DSPAM-Confidence:'):
            print(line)
            index = line.find(':')
            total += float(line[index + 1: ])
            count += 1

    print("Total: " ,total)
    print("Average: ", total/count)


file_name = input("Enter the file name \"either mbox-short.txt or words.txt\": ")
file_name = r'./files/'+file_name
count = 0

try:
    with open(file_name,'rt') as file:
       for line in file:
           count += 1
       print("There are ",count," lines in the document")
except:
    if file_name == r'./files/na na boo boo':
        print("Na Na BOO BOO TO YOU - gat ya!")

