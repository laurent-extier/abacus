import math

class Util(object):
    def __init__(self):
        self
    
    @classmethod
    def perimeter(cls, shape, *args):
        perimeter = 0
        if shape == "square":
            perimeter = args[0] * 4
        elif shape == "rectangle":
            perimeter = reduce(lambda x, y: (2 * x) + (2 * y), args)
        elif shape == "circle":
            perimeter = 2 * math.pi * args[0]
        else:
            print "The shape, %s, is not supported" % (shape)
        return perimeter
        

    @classmethod
    def area(shape, *args):
        pass

    @classmethod
    def volume(arg1, arg2, arg3):
        pass

    @classmethod
    def speed(arg1, arg2):
        pass

    @classmethod
    def distance(arg1, arg2):
        pass

    @classmethod
    def time(arg1, arg2):
        pass
