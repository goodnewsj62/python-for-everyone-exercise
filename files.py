# r'C:Users\Goodnews\Downloads\uPyCraft_V1.1','rt'

with open(r'C:\Users\Goodnews\Documents\termpaper.txt', 'rt') as f:
    data = f.read()
    print(data)

print(data)

with open(r'C:\Users\Goodnews\Documents\experiment.txt', 'rt', encoding='latin-1', newline='', errors='ignore') as b:
    print(b.read())

# separating print statement of different values with sep keyword argument
# specifing ending could be done by using end

print('\nHello world!', 'Ace', 5, 87, sep=',')
test = ('Ace', 5, 87)
print(*test, sep=',')

for n in range(5):
    print(n, end=' ')

with open(f'./test_files/feature_tests.bin', 'rb') as f:
    data = f.read().decode(encoding='latin-1')

print(data)

# import array
#
# new = array.array('i',[0,0,0,0])
# with open(f'feature_tests.bin', 'rb') as f:
#     data = f.readinto(new)
# #some binary files can be read into others using the readinto method
# print('new: ', new)
# print('bin: ', data)

import os

if not os.path.exists("./test_files/feature_tests.bin"):
    with open('./test_files/feature_tests.bin', 'wb') as f:
        f.write(data.encode('latin-1'))
else:
    print('file exists')

# you want to check if file exists before writing to it?
# then you can do it with the method above or the method below


# ------------------------------------------------------
# with open('ask.txt', 'xt') as f:
# f.write('yes i just want to test this')

# if file exists it raises an error message

# you could use the StringIO or ByteIO to mimic files
import io

text_1 = io.StringIO()
text_1.write("you are great")
# you can also write it this way
print("Hello world", file=text_1)

print(text_1.getvalue())

text_1 = io.StringIO('Hello World')
print(text_1.read())
print(text_1.read(4))

# # you can also read and write from zip/compressed file using import gzip, bz2
# import gzip,bz2
#
#
# with gzip.open('test_zip.gz' ,'xt') as f:
#     f.write('just testing')

from functools import partial

# so we can read programs in chunks or bit by bit with the function tool
# partial is used to make the file a callable fot the iter() function  so the file .can be read in size of 16 bits
# then the for loop goes through the records which each line is 16 of text
# r'' is the sentinel is returned at the end of the file
# this solution is most useful for reading binary file


RECORD_SIZE = 16
with open('./test_files/ask.txt', 'rt') as file:
    records = iter(partial(file.read, RECORD_SIZE), r'')
    for r in records:
        print(r)


# a buffer is a  temporary memory storage where data can be stored during processing or during transfer to hold data right before it ris used
# for example if you are watching some videos on youtube 20% of the data has been transferred into the buffer
# so you can watch that until other parts get transferred

# the bytearray() takes the file size as the buffer size in bits then the  file ris readinto the buffer "buf"
# then we test what we have wrote

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as file:
        file.readinto(buf)
    return buf


with open('./test_files/somefile.bin', 'wb') as f:
    f.write(b'this is just a test')

buf = read_into_buffer('./test_files/somefile.bin')

print(type(buf))
with open(r'./test_files/newfile.bin', 'wb') as newfile:
    newfile.write(buf)

with open(r'./test_files/newfile.bin', 'rb') as newfile:
    read_data = newfile.read()
    print(read_data)
# CAUTION : using readinto is for only arrays so do not write less than the buffer size or array size if not it
# might be read as corrupt by the computer

# another way of using this feature is by using the memoryview() function which will give you a zero copy due to
# it accesses the memory address of the bytearray so you can write directly to the address there eby changing the value\
# memory view is only for byte like objects

l = bytearray(19)
m1 = memoryview(buf)
m2 = m1[-5:]
print(m1, m2, end='')
m2[:] = b' TEST'  # the space ' ' is left because we need the byte equal to m2

print('\n', buf)
# caution: always use the slice[] to ork with memoryview eg m2 = b' TEST' is wrong and m2 = m1 is wrong

size = 1000
# the seek() function allocates the size of value
with open('./test_files/data', 'wb') as file:
    file.seek(size - 1)
    file.write(b'\x00')

# this could be used to read lines depending on the hint given. it returns a list containing each line
with open('./test_files/ask.txt', 'r') as f:
    print(f.readlines(36))

# ------------------------------------------------------------------------------------------------------
# manipulating files and file-path with the os module

# You can make a directory automatically using this
os.makedirs('./test_files/makedir_test')
# this could be used to remove a dir
os.removedirs('./test_files/makedir_test')
# this could be used to remove or delete a file
os.remove('./test_files/data')
# This could be used to get system environment variable
hold_path = os.environ.get('PATH')
# i guess you know why we can write and access environment using that method:This is because the environment
# variables are dictionary variables

print(hold_path)
# you can also write or create  to the system environment this way
# os.environ['EMAIL_OF_USER'] = 'osonwajohn@gmail.com'

os.system('cd c:')

# gets the directory name which the file is within
hold_dir_name = os.path.dirname('./venv/lib/site-packages/setuptools-40.8.0-py3.7.egg')
print('--->: ',hold_dir_name)

# gets the basename or the file in the folder
hold_base = os.path.basename('./venv/lib/site-packages/setuptools-40.8.0-py3.7.egg')
print('-->: ', hold_base)

# to join directories we use
new_dir = os.path.join('hey/good','test.csv')
print('-->: ',new_dir)

# to get the default user path
# you must include ~ in front
user_sys_path = os.path.expanduser('~\practice')
print('-->: ',user_sys_path)

# to get the extension from a file sperated
exten = os.path.splitext('~/test_files/ask.txt')
print('-->: ', exten)

# you can also split last path from others
split_dir_or_file = os.path.split('~/test_file/ask.txt')
print('-->: ',split_dir_or_file)

#you can also if a file, dir,path exist
exist = os.path.exists('./yop/hey')
print('---:', exist)
exist = os.path.exists('./test_files/ask.txt')
print('---:', exist)

is_file = os.path.isfile('./test_file/ask.txt')
print('---: ',is_file)
is_file = os.path.isfile('./test_file')
print('---: ',is_file)

is_dir = os.path.isdir('./test_files/ask.txt')
print('---: ',is_dir)
is_dir = os.path.isdir('./test_files')
print('---: ',is_dir)

# you can get the filesize, create-time, modified-time and so on
file_size = os.path.getsize('./venv/lib/site-packages/setuptools-40.8.0-py3.7.egg')
print('***: ', file_size)

create_time = os.path.getctime('./venv/lib/site-packages/setuptools-40.8.0-py3.7.egg')
print('***: ', create_time)

# you can use it this way in a more reasonable manner
import time
create_time = time.ctime(os.path.getctime('./venv/lib/site-packages/setuptools-40.8.0-py3.7.egg'))
print('***: ', create_time)

modified_time = time.ctime(os.path.getmtime('./venv/lib/site-packages/setuptools-40.8.0-py3.7.egg'))
print('***: ',modified_time)

# you can use the islink to check if the path given is a link
os.path.islink('')

# get absolute path
print(os.path.abspath(__file__))

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# you can get the list of file
print(os.listdir('./test_files'))

# filters only files
li = [n for n in os.listdir(str(os.path.dirname(os.path.abspath(__file__)))) if os.path.isfile(os.path.join(r'C:\Users\Goodnews\PycharmProjects\practice',n))]

print(li)

# The glob function can be used to filter files of a particular extension
# The fnmatch could be used to filter files of same extension
# note there is need to use the * to unpack files

import glob
from fnmatch import fnmatch

test_glob = glob.glob('./test_files/*py')
print(test_glob)

pyfile = [name for name in os.listdir(str(os.path.dirname(os.path.abspath(__file__)))) if fnmatch(name, '*.py')]
print(pyfile)

# You can shortcut some certain things using stat() to filter out th name size, modified time and so on

filt = glob.glob(str(os.path.dirname(os.path.abspath(__file__)))+'/*.py')
test_stat = [(name,os.stat(name))  for name in filt ]

for name,stat in test_stat:
    print(name,stat.st_mtime,stat.st_size)

# to print file that does not have default encoding you can use the byte string to bypass he encoding

A = [1,4,5,6, 2,3]
B = [0,1,8,5,6]
C = [6,7,8,9,10,11,1]

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
        mid = (low+high)//2
        len_index = (len(inp) - 1) % 2

        if len_index  > 0:
            forward = inp[mid + 1]
            backward = inp[mid - 1]
            if forward < inp[mid] and backward > inp[mid]:
                high = mid
            elif forward > inp[mid] and backward < inp[mid]:
                low = mid
            elif forward < inp[mid] and backward < inp[mid]:
                return inp[mid]


        elif len_index == 0:
            forward = inp[mid + 1] if mid + 1 < len(inp) else float("inf")
            backward = inp[mid - 1] if mid - 1 > 0 else float("-inf")
            if forward < inp[mid] and backward > inp[mid]:
                high = mid - 1
            elif forward > inp[mid] and backward < inp[mid]:
                low = mid + 1
            elif forward < inp[mid] and backward < inp[mid]:
                return inp[mid]



ans = find(C)
print(ans)




