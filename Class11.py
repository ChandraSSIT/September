# Arguments/parameters

# Positional arguments
# keyword arguments
# default arguments
# arbitrary arguments
# keyword arbitrary arguments

# Positional arguments
# we need to pass the data in the same order of parameters defined
def add(a,b):
    result = a+b
    print("value of a " , a)
    print("value of b ",b)
    print(result)

def customerdetails(name,id,balance,bankname='hdfc'):
    customer  = {'name':name,'Id':id,"Balance":balance,'Bankname':bankname}
    print(customer)

add(3,4)
customerdetails(2234,'chandra',35345)

# keyword arguments
customerdetails(balance=324324,id=123243,name='chandra')

# default arguments
customerdetails('akbar',432423,233)
customerdetails('akbar',432423,233,'ICICI')

# arbitrary arguments

def add(a,b,*args,c=10):
    result = a+b+c
    print("a value ",a)
    print("b value ",b)
    print("c value ",c)
    print("args value ",args)
    for i in args:
        result += i
    print(result)

add(2,3,4,5,6,7,8)
add(2,3,4,5,6,7,8,9,11,12,13,14,15)
add(2,3)
add(2,3,4)

# keyword arbitrary arguments

def add1(a,b,*args,c=10,**kwargs):
    print("value of a ",a)
    print("value of b ",b)
    print("value of c ",c)
    result = a+b+c
    print("value of args ",args)
    print("value of kwargs ",kwargs)
    for i in args:
        result +=i
    for j in kwargs:
        result += kwargs[j]
    print(result)


add1(2, 3, 4, 5, 6, 7, d=4545, e=45, f=45, g=65)

# order of arguments (positional,default)=> positional,default
# order of arguments (positional,default,arbitrary)=> positional,arbitrary,default
# order of arguments (positional,default,arbitrary,keyword arbitrary)=> positional,arbitrary,default,key
# word arbitrary


# define method to create list of customers
# define one method which will give all customers












