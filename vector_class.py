

class Vector:
    """ this imlements a vector with n dimension making servernal operation """
    def __init__(self, dimension):
        if dimension < 4:
            self._dimension = dimension
            self._coordinate = [0] * self._dimension
        else:
            print('!!!Enter a dimension less than four!!!')

    def __getitem__(self, item):
        return self._coordinate[item]
    def __setitem__(self, item, value):
        try:
                self._coordinate[item] = int(value)
        except ValueError:
            print("-----------------Please enter digits-------------------!!")
        except IndexError:
            print("---------------This index does not exist--------------------!!")


    def __len__(self):
        return len(self._coordinate)
    def __add__(self, other):
        try:
            result = Vector(len(self))
            # This will assign a class of zero vector with original first dimension
            # to result
            for each in range(len(self)):
                result[each] = other[each] + self[each]

            return result

        except ValueError:
            print("value must be either integers or floating points")
        except IndexError:
            print('dimension must be the same!!')
        finally:
            print('--------------Enter a vector---------------------')

    def __neg__(self):
        result = Vector(len(self))
        for each in range(len(self)):
           result[each] = self._coordinate[each] * -1
        return result
    def __eq__(self, other):
        return self._coordinate == other
    def __ne__(self, other):
        return not self._coordinate == other

    def __lt__(self, other):
        return not self._coordinate > other

    def __str__(self):
        return '{}i + {}j + {}k'.format(self._coordinate[0],self._coordinate[1],self._coordinate[2])

    def __sub__(self, other):
        try:
            result = Vector(len(self))
            for each in range(len(self)):
                result[each] = other[each] - self._coordinate[each]
        except TypeError:
            print("must be of same type integer/decimal!")
        except ValueError:
            print("value must be either integers or floating points")
        except IndexError:
            print('dimension must be the same!!')
        finally:
            print('--------------Enter a vector---------------------')

    # def __radd__(self, other):
    #     try:
    #         result = Vector(len(self))
    #         # This will assign a class of zero vector with original first dimension
    #         # to result
    #         for each in range(len(self)):
    #             result[each] = self[each] + other[each]
    #
    #         return result
    #
    #     except TypeError:
    #         print("must be of same type integer/decimal!")
    #     except ValueError:
    #         print("value must be either integers or floating points")
    #     except IndexError:
    #         print('dimension must be the same!!')
    #     finally:
    #         print('--------------Enter a vector---------------------')



if __name__ == '__main__':
    vec1 = Vector(3)
    vec2 = Vector(3)
    vec3 = Vector(2)


    vec1[0] = 3
    vec1[1]= 6
    vec1[2] = 2

    vec3[0] = 3
    vec3[1] = 6



    print(vec1)
    print(vec1[0])
    print(len(vec1))
    vec2[0] = 2
    vec2[1] = 6
    vec2[2] = 1


    print(vec1 + "")
    print(vec1 < vec2)
    print(vec2 != vec1)
    print(vec3 == vec1)

    for each in range(len(vec3)):
         print('iterating------')
         print(vec3[each])
    print(vec2- vec3)
    print(-vec2)
    f = vec1 + [1,2,3]
    print(f)

