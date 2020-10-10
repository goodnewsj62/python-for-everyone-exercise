# You can use the magic method repr to represent values or data of a class
# repr stands for representation. for example take for instance the class below

class Grade:
    ''' This takes in your score and gives the grade'''
    def __init__(self, name, score):
        if len(name) > 1:
            name = str(name)
        else:
            raise ('INVALID NAME')

        try:
            score = int(score)
        except:
            score = 0
            print('please enter numbers')

        if score < 0 or score > 100:
            raise ('Score is INVALID')
        self._name = name
        self._score = score

    def grade(self):
        if self._score < 40:
            return 'F'
        elif self._score < 45:
            return 'E'
        elif self._score < 50:
            return 'D'
        elif self._score < 60:
            return 'C'
        elif self._score < 70:
            return 'B'
        else:
            return 'A'


    def __repr__(self):
        return 'pair({0._name!r},{0._score!r})'.format(self)
    def __str__(self):
        return 'name: {0._name!s}, score: {0._score!s}'.format(self)



grade_test = Grade('goodnews','john')
print(grade_test.grade())
print(grade_test.__repr__())
print(grade_test)


# how to create a factory pattern
# you can make a function that takes in argument as a string to initialize a class and create different instances/objects on a fly

class Circle:
    def __init__(self, raduis = 0):
        self._raduis = raduis

    def print_shape(self):
        print(self._raduis)
class Square:
    def __init__(self, side_length = 0):
        self._side_lenght = side_length

    def print_shape(self):
        print(self._side_lenght)

def factory(inp,*args,**kwargs):
    context = {'circle':Circle, 'square':Square}
    return context[inp](*args,**kwargs)

a = factory('circle')
a._raduis = 15
print(a._raduis)



date_format = {
    'ymd':'{d.year},{d.month},{d.day}',
    'dmy':'{d.day},{d.month},{d.year}',
    'dym':'{d.day},{d.year},{d.month}',
}

class DateT:
    def __init__(self, year, month, day):
        self.year = year
        self.day = day
        self.month = month
    def __format__(self, obj):
        if obj ==  '':
            obj = 'ymd'
        code = date_format[obj]
        return code.format(d = self)

dat = DateT(2020,10,23)


# with magic methods like __enter__ and __exit__ you can be able to make use of the python with statement

from socket import socket,AF_INET,SOCK_STREAM

class Connect:
    def __init__(self, address,port):
        self.address = (address,int(port))
        self.sock = None

    def __enter__(self):
        if self.sock != None:
            raise RuntimeError('Already connected!')
        self.sock = socket(AF_INET,SOCK_STREAM)
        self.sock.connect(self.address)
        return self.sock
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None

# when you use this in a with block the __enter__ method is called at the beginning of the lock(with ) and the __close__
# is called at the end of the with block.
from functools import partial

# with Connect('www.python.org',80) as f:
#     # connection created: __enter__ called
#     f.send(b'GET /index.html/1.0\r\n')
#     f.send(b'Host: www.python.org\r\n')
#     f.send(b'\r\n')
#     resp = b''.join(iter(partial(f.recv, 8192), b''))
#     # connection closed: __exit__ called

# you can use the __slot__ when you want to assign a large number of instance/attributes and save memory

class Show:
    __slots__ = ['name','class_','score','rating','table','address','number','availability','money_won']
    def __init__(self,name,class_,score,rating,table,address,number,availability,money_won):
        self.name = name
        # and so on


# using the @property method you can assign values to instances of a class with the equal(=) sign or
# you can do a get method and set method like normal operations
# please you don't use @property any how or any time you like, you use this whenever you want to check
# or validate some input to the class method if not you can try __setitem__ or __getitem__
# you can also use the @property method for coding


class Person:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    @property
    def first_name(self):
        return self.name
    @first_name.setter
    def first_name(self,nam):
        if not isinstance(nam,str) :
            raise ValueError("must be a string")
        self.name = nam



    @first_name.deleter
    def first_name(self):
        self.name = ''


person_test = Person('goodnews','john')

# if you notice we called the first_name method without the parenthesis () and assigned with the = sign
print(person_test.first_name)
person_test.first_name = 'marvellous'
print(person_test.first_name)


setattr(person_test,'name','Rose')
print(person_test.first_name)


# we can also use super to call methods in the parent class if we inherited a class in our written class
