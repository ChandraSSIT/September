# Decrotators

# in python everything is an object ,
x = 5
name = 'chandra'
l1 = [1, 2, 3, 4]


# This is function is used get banker details
def function1():
    """ This is used to get banker details """
    return 0


print(function1.__doc__)


# decorator => extending the functionality of a function by passing function as an object to
# the other function , by using this passed function result we can extend the result

def calculator(func1):
    def inner1(a, b, c):
        print("I am inside decorator")
        if c == 'A':
            if a < b:
                a, b = b, a
            result = func1(a, b)
            print("result from decorator", result)

    return inner1




@calculator
def sub(a, b):
    return a - b


# sub(2, 4,'B')


# Module and import

# module is nothing but a python file which contains variables,functions and classes
from Class12 import getnumber

getnumber()


# anonymous function

def evennumber(n):
    return n % 2 == 0


# lambda => anonymous function , which will not have function name

a = lambda x, y: x * y

print(a(3, 3))

#
l1 = [1, 2, 3, 4, 5, 6]

# evens = filter(evennumber, l1)
evens = filter(lambda x: x % 2 == 0, l1)
print(list(evens))

all = map(lambda x: x % 2 == 0, l1)
print(list(all))


l2 = ['a','b','c','d']
l2.pop(1)
l2.pop()
# l2.remove('a')
print(l2)


