# Local variable and global variable

# Local variable
#  The variable which ever is declared inside the function is called local variable , the scope of this
# variable will be to that function

#  Global variable is nothing but which can be accessed to every one in the file

#  Global variable
y = 10
def getnumber():
    # local variable
    x = 5
    global z
    global y
    y = 12
    z =10
    print(x)
    print("inside function", y)

getnumber()
# print(x)
print(y)
print(z)


customers = []
def createcustomer(name,id,balance,bankname):
    customer = {'name':name,"ID":id,"Balance":balance,"Bankname":bankname}
    customers.append(customer)


def getcustomers():
    return customers

createcustomer('john',123,313123,'hdfc')
createcustomer('abc',333,313123,'icici')
createcustomer('mohan',2433434,313123,'icici')

# print(getcustomers())

# function inside a function

def sample():
    def innerfunc1(a,b):
        return a+b

    return innerfunc1


aa = sample()
bb = aa(3,4)
print(bb)



# generators, iterators,decorators


print("/////Iterators////")
# Iterators
l1 = ['chandra','mohan','akbar','latha','nag']

iterobj = iter(l1)
print(next(iterobj))
print(next(iterobj))
print(next(iterobj))
print(next(iterobj))
# print(next(iterobj))

# for i in l1:
#     print(i)

# Enumerate
for i in enumerate(l1):
    print(i)

def generatorsample():
    # l1 =[]
    for i in range(4):
        # l1.append(i)
        yield i
    # return l1

print(list(generatorsample()))

for i in generatorsample():
    print(i)

from Class13 import  function1

print(function1.__doc__)

