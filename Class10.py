# functions

# defined a function , even numbers is the function name .signature => it defines the parameters/arguments
# it contains a block of a code
# we have to pass the parameters
def evennumbers(num):
    for i in range(num):
        if i % 2 == 0:
            print(i, end=" ")
    print(" ")


# how to use this function or how to call this function
evennumbers(10)
evennumbers(30)
evennumbers(50)

def checkisevennumber(num):
    if num % 2 == 0:
        return True
    else:
        return False

def allevennumber(num):
    for i in range(num):
        if checkisevennumber(i):
            print(i, end=" ")
    print(" ")

def checkisprime(num):
    if num >= 2:
        if num == 2:
            return True
        else:
            for j in range(2, num):
                if num % j == 0:
                    return False

            return True
    else:
        return False

def primenumbers(rangeofnumber):
    for num in range(0,rangeofnumber):
       if checkisprime(num) :  # calling a function inside other function
           print(num,end=" ")
    print("")


primenumbers(40)


# Arguments/parameters
# Positional arguments
# keyword arguments
# default arguments
# arbitrary arguments
# keyword arbitrary arguments


