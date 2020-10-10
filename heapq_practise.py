# you can get the list of n items which are sorted in a particular order
# e.g: either max or min( that is n number of maximum or n number ist of minimum)
# for example: for a list of [1,2,3,4,5] you can get the two highest value
# [4,5] with heapq.nlargest(2,list_foo) or the lowest with nsmallest(2, list_foo)
# , other functions include the heapify: arranging the list of items that are
# order as heap. the heappop renders the smallest item
#just fun to really try out

import heapq


num = [1,2,3,-8,6,7,8,99,9,9,0]
store = heapq.nlargest(3,num) #gives the first three largest number
print(store)

# for a more complex list with dictionaries
data = [
    {'name': 'Abu','department':'commercial','grade':'B'},
    {'name': 'Alex','department':'science','grade':'C'},
    {'name': 'josh','department':'science','grade':'A'},
    {'name': 'Ali','department':'arts','grade':'E'},
    {'name': 'rachel','department':'science','grade':'A'},
    {'name': 'Abraham','department':'science','grade':'B'},
    {'name': 'Tasha','department':'science','grade':'F'}
]

upper_grade = heapq.nsmallest(4,data,key = lambda s: s['grade'] )# the key let us get these by the grades
print(upper_grade)

class PriorityQueue:
    def __init__(self):
        self._value = []
        self._index = 0

    def push(self,items,priority):
        heapq.heappush(self._value, (-priority,self._index,items))
        # the  item above is a tuple which allows your priority
        #eg 5 to become -5 making it the lowest therefore when sorting with heappop
        # the tople with highest number eg 5 comes first
        self._index += 1
        # helps when it comes to comparing items

    def pop(self):
        return heapq.heappop(self._value)[-1]


class item:
    def __init__(self,inp):
        self._inp = inp
    def __repr__(self):
        return 'item({})'.format(self._inp)


if __name__=="__main__":
    q = PriorityQueue()
    hold_inp = {'hi':1,'hey':4,'foo':5,'mate':2}
    for x,y in hold_inp.items():
        # assign values to init method in item class and then
        # assign both priority and item to the  push method
        q.push(item(x),y)
    for each in range(len(hold_inp)):
        print(q.pop())

