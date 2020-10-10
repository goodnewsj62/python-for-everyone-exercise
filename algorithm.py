A = [6, 7, 1, 2, 3, 4, 5]  # thisb is a cyclically shifted array


# to find the lowest number using binary search


def find(A):
    low = 0
    high = len(A) - 1
    while low < high:
        mid = (low + high) // 2

        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] < A[high]:
            high = mid - 1

    return low


hold = find(A)
print(hold)
print(A[hold])

# second example with bitonic sequence
# a bitonic sequence is one which increases to it higest point and
# then it reduces afterwards
# mathematically this can be written in this form
# x_0<= .... <= x_k >= ....<= x_n-1  where k, 0<=k < n "<---- these are
# referring to index"


A = [1, 4, 5, 6, 2, 3]
B = [0, 1, 8, 5, 6]
C = [6, 7, 8, 9, 10, 11, 12]


# we could solve this problem using our normal for loop going through the eleme
# -nt one after the other but this is naive way of doing so because the time
# use to get the result will increase as the number of element increases
# this is called the linear search method. for example take a list b = [0,1,2
# ....9999,1,3,4,5] solving this problem using linear search is not really ideal
# or the best, instead we can use binary search to do this

def find(inp):
    # a list of length 1 or 2 can never be a bitonic sequence cause it wont obey
    # the priciple, so we check of that
    if len(inp) < 3:
        return None
    low = 0
    high = len(inp) - 1
    while low <= high:
        mid = (low + high) // 2
        len_index = len(inp) - 1

        if len_index % 2 == 0:
            forward = inp[mid + 1] if mid + 1 < len(inp) else float("inf")
            backward = inp[mid - 1] if mid - 1 > 0 else float("-inf")

            if forward < inp[mid] and backward > inp[mid]:
                high = mid - 1
            elif forward > inp[mid] and backward < inp[mid]:
                low = mid + 1
            elif forward < inp[mid] and backward < inp[mid]:
                return inp[mid]
        else:
            print("yes")
            forward = inp[mid + 1]
            backward = inp[mid - 1]
            if forward < inp[mid] and backward > inp[mid]:
                high = mid
            elif forward > inp[mid] and backward < inp[mid]:
                low = mid
            elif forward < inp[mid] and backward < inp[mid]:
                return inp[mid]


ans = find(A)
print(ans)

# -----------------------------binary search-------------------------
# we want to use binary search to get the fixed point of some array
# fixed point is were an index i equals A[1]
# The items are supposed to be sorted
#    0  1  2  3 4 5 6
A = [-3, -2, -1, 1, 4, 6, 7]
B = [0, 2, 5, 8, 7]
C = [-1, 1, 2, 3, 5, 6, 7]
D = [-1, 3, 4, 7, 5, 8, 6]


def find_fixed_point(A):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2

        if A[mid] > mid:
            high = mid - 1
        elif A[mid] < mid:
            low = mid + 1
        elif A[mid] == mid:
            return mid

    return None


print(find_fixed_point(D))

# we want to use the idea of binary search to find the square that is less or e
# -ual to the integer that is taken as an argument

inp = 12
num = 300


# 1*1 = 1
# 2*2 = 4
# 3*3 = 9
# 4*4 = 16
# 5*5 = 25
# 6*6 = 36

def find_square(num):
    low = 0
    high = num
    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared > num:
            high = mid - 1
        elif mid_squared < num:
            low = mid + 1
    return high


print(f'the square root of {inp} is', find_square(inp), sep=': ')
print(find_square(300))

# the common built in python library for binary serch is the bisect module
# it has the methods bisect_right(), bisect_left(),insort_left() and insort_right()
# bisect_right() get the first-occurance index of a target while that of right get
# the index after the target for insertion, the insort works like the bisect
# right and left but they only used to insert element at index positions

import bisect

# using greedy algorithm for optiomal task assignment
# lets take for example we want to optimally share task between three workers
# a,b,c.The working hour of each task is [5,6,2,3,4,3], to share the working
# hours between the workers optimally we have to pair the lowest with
# the highest hour: therefore a gets (x,y), b gets(x1,y1),c gets(x2,y2)
# that is (6 + 2), (5 + 3), (4 + 3). but before we do this we will sort the
# list


A = [5, 6, 2, 3, 4, 3]
A.sort()


# note the symbol ~in front of an index gives the opposite index
# for example: where i = 0,j = 1 A[~i] = A[-1] and A[~j] = A[-2]


def greedy_algo(A, idx=0):
    end = len(A) // 2
    newlist = []
    while idx < end:
        newlist.append(A[idx] + A[~idx])
        idx += 1
    return newlist


print(greedy_algo(A))

# this below is a sorting algorithm that will get the intersection between
# two list a and b

A = [1, 3, 4, 5, 5, 6, 7, 11]
B = [2, 3, 4, 7, 8, 10]


def my_intersection(A, B):
    i = 0
    j = 0
    return_list = list()
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                return_list.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1

    return return_list


print(my_intersection(A, B))

# there is also a way you can do this with sets
A =  set(A)
B = set(B)

print(A.intersection(B))


# algorithm to solve if a two strings are permutations of each another

# time complexity is O(n)
# space complexity is O(n)
def is_permutation(inp_1 , inp_2):
    inp_1 = inp_1.lower()
    inp_2 = inp_2.lower()

    if not len(inp_1) == len(inp_2):
        return False
    dic = dict()

    # the get method takes the key of dictionary and a default value
    # if key does not have a value it gives it the default value
    # else it just returns the value of the key
    for i in range(len(inp_1)):
        dic[inp_1[i]] = dic.get(inp_1[i],0) + 1
    for i in range( len(inp_2)):
        dic[inp_2[i]] = dic.get(inp_2[i],1) -1
    return all(value == 0 for value in dic.values())


print(is_permutation('hey','hey'))



# an algorithm to check if two different string are anagrams

def is_anagram( str_1 , str_2):

    str_1 = str_1.replace(" ","").lower()
    str_2 = str_2.replace(" ", "").lower()

    if not len(str_1) == len(str_2):
        return False

    hold = dict()
    length = len(str_1)
    for n in range(length):
        hold[str_1[n]] = hold.get(str_1[n], 0) + 1
    for n in range(length):
        hold[str_1[n]] = hold.get(str_1[n], 1) -1
    return all(value == 0 for value in hold.values())


print(is_anagram('fairy tales', "road safety"))



# checks if string is a permutation of a palindrome or a palindrome

# a palindrome usually have a repitition of all letters except one letter eg wow race car taco cat


# time complexity O(n)
# space complexity O(n)
def is_palindrome(strng):
    strng = strng.replace(" ","").lower()
    hold = dict()
    ood = 0
    for each in range(len(strng)):
        hold[strng[each]] = hold.get(strng[each], 0) + 1
    for key,value in hold.items():
        if value % 2 == 0:
            pass
        elif not value % 2 == 0:
            ood += 1
    if ood == 1 or ood == 0:
        return True
    return False



print(is_palindrome('race car'))

import os
print('OPEN_WEATHER_API' in os.environ)