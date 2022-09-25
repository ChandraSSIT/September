# operators
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators

# Arithmetic operators
# +,-,*,/,%,**,//

a = 3
b= 4
c = a+b
print("addition-",c)
print("subtraction",a-b)
print("multiplication",a*b)
print("division",b/a)
print("modulation",b%a)
print("exponential",a**4) # a*a*a*a
print("floor divison",1244//10) # 1244//10 => 124

# Assignment operator

d = 5
d = d + 4
print(d)

d += 5  # d = d+5
print("+=",d)
d -= 3 # d = d-3
print("-=" , d)
d *=2
print("*=",d)
d /=2
print("*/",d)

# Comparison operator
a= 5
b =4
#  == , != , < ,> ,<=,>=
print(a==b) # if both values are same it will give True , otherwise False
print(a!=b) # if both values are not same it will give True , otherwise False
print(a < b) #if a is lesser than b it will give true else false
print (a>b)  # if a is greater than b it will give true else false
c = 4
d = 5
print(c<=d) # if a is lesser than or equal b it will give true else false
print(a>=b) # if a is greater than or equal b it will give true else false

# Logical operators
# and , or , not
x = 5

# True and True => True
# False and False => False
# True and False => False
# False and True => False
print("////and ////")
print(x >2 and x < 6) # True and True => True
print( x == 4 and x < 6) # False and True => False
print( x > 2 and x <4) # True and False => False
print(x == 2 and x >10) # False and False => False

print("/////or////")
# or
# True and True => True
# True and False => True
# False and True => True
# False and False => False
print(x >2 or x < 6) # True and True => True
print( x == 4 or x < 6) # False and True => True
print( x > 2 or x <4) # True and False => True
print(x == 2 or x >10) # False and False => False

# not
print("////not////")
x = 5
print( not(x > 4))

# Identity operators
x = 5
y = x
print("/////identity")
# is , is not
print(x is y)
print( x is not y)

# Membership operator
# in , not in
print("/// membership")
l1 = [ 1,3,4,5,6]
print(3 in l1)
print(11 in l1)
print(11 not in l1)
dic1 = {'name':'chandra','address':'ATP'}
print('name' in dic1.keys())


