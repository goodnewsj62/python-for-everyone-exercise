# import random
# import time
#
# class Bear:
#     def name(self):
#         return 'bear'
# class Fish:
#     def name(self):
#         return 'fish'
# river = []
# def create_river(Bear,Fish):
#     river = []
#     for n in range(100):
#         river.append(random.choice([Bear,Fish,None]))
#     return  river
#
# river = create_river(Bear(),Fish())
#
#
# while True:
#     b = river.index(None)
#     print(river[b])
#     time.sleep(5)
#     for animal in range(99):
#         if river[animal] !=  None and river[animal+1] != None:
#             if river[animal].name() == 'bear' and river[animal + 1].name() == 'fish':
#                 time.sleep(1)
#                 print(river[animal].name(),' is going to the river')
#                 time.sleep(1)
#                 print('bear saw a fish ')
#                 time.sleep(0.5)
#                 print('eats the fish\n\n')
#                 del river[animal + 1]
#                 river.append(Fish())
#
#             elif river[animal].name() == 'bear' and river[animal + 1].name() == 'bear':
#                 time.sleep(1)
#                 print(river[animal].name(),' is going to the river')
#                 time.sleep(1)
#                 print('bear saw another bear \n\n')
#                 if None in river:
#                     hold = river.index(None)
#                     river[hold] = Bear()
#
#             elif river[animal].name() == 'fish' and river[animal + 1].name() == 'fish':
#                 time.sleep(1)
#                 print(river[animal].name(),' is in  the river')
#                 time.sleep(1)
#                 print('fish saw another fish \n\n')
#                 if None in river:
#                     hold = river.index(None)
#                     river[hold] = Fish()
#
#     river = create_river(Bear(),Fish())



# print("""
#         choose from these options
#         1. Purchase a book
#         2. Read a book
#         3. view list of purchased books
#      """)
# try:
#     choice = int(input('Please choose from the options: '))
# except ValueError:
#     print('Please Enter a value')
#
#
# if choice == 1:
#     pass
# if choice == 2:
#     pass
# if choice == 3:
#     print("You have no purchased book")

# data =[{"numeric": 3093,"string": "data testing","float": 8.90,"bool": True}]
# import json
#
# # this overwrites the json content in the json files
# with open('practice.json','w') as file:
#     json.dump(data, file)
#
# print(data)
from abc import ABCMeta, abstractmethod
from math import sqrt,pow

class Polygon(metaclass = ABCMeta):
    ''' this is the blueprint base class of the polygon sub classes'''

    '''the implementation of the class below will be done in the child class'''
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass


class Quadelateral(Polygon):
   pass
class Triangle(Polygon):
    def __init__(self,base,height):
        try:
            self._base = float(base)
            self._height = float(height)
        except:
            print("enter an integer or a decimal ")

    def area(self):
        return 0.5 * self._base * self._height

    def perimeter(self):
        hyp = sqrt(pow(self._height, 2) + pow(self._base, 2))
        p = hyp + self._height + self._base
        return p
class Hexagon(Polygon):
    def __init__(self,len_iof_side):
        try:
            self._lside = float(len_iof_side)
        except:
            print("enter an integer or a decimal ")

    def perimeter(self):
        return self._lside * 6

    def area(self):
        #fomular for area of hexagon = 1/2 perimeter * apothem
        # where apothem = 1/2 side * sqrt(3)
        apothem = (self._lside/2) * sqrt(3)
        return 0.5 * self.perimeter() * apothem
class Octagon(Polygon):
        pass
class Pentagon(Polygon):
    pass
class Rectangole(Polygon):
    pass


self = Hexagon('hhhhh')
print(self.area())
