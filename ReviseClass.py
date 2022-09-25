# Variables, Datatypes,operators,Conditional statements , loop statements
# its stores some data in memory , for that we need some address or identifier
x = 10
print(x)
x = 15
y  = 40

print(x+y)
print(x-y)
print(x*y)

name ='chandra'
print(name)
name ='chandra mohan'
print(name)

balance = 32432.33
ispersonexists = True

# data types
# python is dynamically typed

name = 'chandra'
address = '656/77,ATP'

accountnumber = 123455555
balance = 23434.33

# primitive types => string , int ,float, bool
# Sequence type => list , tuple , set , dict
print( type(name) )
print( type(address))

print("accountnumber type",type(accountnumber))
print("balance type",type(balance))
isvalid = True
print("isvalid type",type(isvalid))

# data type conversion

balance = 2343243.34
# type  conversion
balupdated = int (balance)
print(balupdated)
print("balupdated type ---- ",type(balupdated))

str1 = '232343'
num = int (str1)


# sequence data types

# grouping of different types  of data
# list , tuple,set,dictionary
# list
# list is mutable/changeable elements inside this can change
l1 = ['chandra',24324324,2343.434,True]
print(l1)
print('l1 type ---- ', type(l1))
# CRUD => create ,read , update ,delete
# create => creating a record
l1 =  ['chandra',24324324,2343.434,True]
# read
# indexing ,slicing

print(l1[0])
print(l1[2])

l2 = [11,22,33,43,45,46,47,98,59,104]

print(l1[-4])
print( l2 [4])
print( l2[-7])

# slicing
print( l2[2:8:1] )
print( l2[2:8:2] )
print(l2[2:8])
print(l2[2:])

# update
print(l1)
l1[0] ='mohan'
print(l1)

l1[1:3] = 333333,44.44
print(l1)

# add new elements
# append => it will add single item
# extend => to add multiple items
l1.append('ATP')
print(l1)
l1.extend(['ATP','2343'])
print(l1)

# del
del l1[2:]
print(l1)
# del l1
# print(l1)

# tuple
# tuple is immutable/unchangeable , its like constant
# CRUD
# Create
t1 = (12,13,45,67,67)
# Read
print(t1[0])
print(t1[2:4])

# update => update will not work for update
# t1[0] = 65

# delete => individual element delete will not work
# del t1[0]
del t1
# print(t1)

# set
# it will remove duplicates
# its unordered
# Create
set1 = {45,78,1,2,3,4,3,4,98,54,65}
print(set1)

# read
# index or slicing will not work
for i in set1:
    print(i)

# update
# with slicing and index it will not work
#  we can't update existing elements
#  we can add new elements
# by using add,update
print(set1)
set1.add(100)
print(set1)
set1.update([400,200,300])
print(set1)

# delete
set1.remove(98)
print(set1)
del set1

# dictionary
# key and value pair
l1 =['chandra',243423,2432423,234343]
dict1 = {}
set1 ={1}
print(type(set1))
print(type(dict1))

# create
dict1  = {'name':'chandra','accountnumber':232342343,'balance':34324 }
# read
print(dict1['name'])
print(dict1.keys())
print(dict1.values())
print(dict1.items())

# update
dict1['name'] = 'mohan'
print(dict1)
dict1['address'] ='ATP'
print(dict1)

# delete
del dict1['name']
print(dict1)
del dict1









