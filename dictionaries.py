from collections import defaultdict,OrderedDict

# you can create multi-valued dictionaries in python using the
# defaultdict from the collection module/library and you can also
# order your dictionary according to the elements entered (first - last)
# using the OrderedDict class from collections library
# note:Always  remember that this OrderedDict size is twice as large
# as the normal dictionary

# example 1
dic = defaultdict(list)
#you can do this with a list or a set
#with a set do: defaultdict(set)

keys = ['a','b','c','d']
index = 0
while index < len(keys):
    for x in range(1, 10):
        dic[keys[index]].append(x)
    index += 1

print(dic)

# you could also do this with a set default method
# as described below
for x in range(1,10):
    dic.setdefault('e',[]).append(x)
    # .setdefault(key,list[] or set{})

print(dic)

# example 2
# the ordered dictionary uses a doubly link list mapping that is
# ordered according to insertion
dic2 = OrderedDict()
dic2['bae'] = 23
dic2['love'] = 24
dic2['foo'] = 26
dic2['boo'] = 25

print(dic2)

# As you can see this can be useful when you want to iterate
# or when you want to serialize or even encode. For example:
import json

data = json.dumps(dic2)

print('json data: ', data)
#lovely right

class SequenceIterator:
    'just practising how to iteration '

    def __init__(self,seq):
        self._sequence = seq
        self._index = -1

    def __next__(self):
        self._index += 1
        if self._index < len(self._sequence):
            return  self._sequence[self._index]
        else:
            raise StopIteration()

    def __iter__(self):
        return self


if __name__ == "__main__":
    test = SequenceIterator([1,2,3,4])

    for x in test:
        print(x)


# with the operator module it becomes easy to sort a list of dictionary by a specific key
# which will help reduce run time of the code.
# another seful library is the itertools wich contain the groupby that can be
# used to iterate through a particlar key in the dictionary. This can also be done
# by the default dict in collection module

from operator import itemgetter
from itertools import groupby

data = [
{'phone': 5678990,'name': 'bucky','date': '07/01/2012'},
{'phone':4567888 ,'name':'chuck','date': '07/04/2012'},
{'phone': 5785494,'name':'josh','date': '07/02/2012'},
{'phone': 4774748,'name':'emma','date': '07/03/2012'},
{'phone': 47484848,'name':'eliza', 'date': '07/02/2012'},
{'phone': 788944,'name':'vanessa', 'date': '07/02/2012'},
{'phone': 48949494,'name':'ugo', 'date': '07/01/2012'},
{'phone': 467448,'name':'solomon', 'date': '07/04/2012'},

]

get_sorted_name = sorted(data, key = itemgetter('name'))
print('sorted name', get_sorted_name)
get_name_date = sorted(data, key = itemgetter('name','date'))
print(get_name_date)

# you can also perform this with the lambda function but the former is faster

get_sorted_date = sorted(data, key = lambda d: d['date'])
print(get_sorted_date)


# to do this we are going to use our groupby from itertools
#you also have to sort the data first to get an expected and more reasonable result

data.sort(key= itemgetter('date'))

for date, items in groupby(data, key = itemgetter('date')):
    print(date)
    for item in items:
        print('',item)


# you can do this also with default dict
new_data = defaultdict(list)

for each in data:
    new_data[each['date']].append(each)

for each in new_data:
    print(each)
    for x in new_data[each]:
        print(' ',x)
    # for inner in [n for n in new_data[each]]:
    #     print(" ", inner)
