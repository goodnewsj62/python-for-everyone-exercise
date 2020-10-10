# the collection built in library support different operations that could be useful
# some examples include: deque :(which is used to store a number of previous value )
# Counter: ( which could give the mode or most frequently occured item pased)
# defauldict : (helps to create multi dictionaries for example 'a':[1,2,3])
# and so on

from collections import Counter, defaultdict,deque

string = "Hey i am going to play an instrument to glorify my father in heaven over the thing he has " \
         "done for me even when i dont know how much he fights for me " \
         "i am going to give him all the praise"

item = []
hold = []
for letter in string:
    if  letter != ' ':
        hold.append(letter)
    else:
        item.append(''.join(hold))
        hold = []



word_count = Counter(item)
most_frequent = word_count.most_common()
print(word_count)

# to update the list you can use the update function
word_count.update(['hey','the','pain','is','for','good'])
print(word_count)

d = deque(maxlen= 3)

for x in range(6):
    d.append(x)
print(d)



