# tuple
# tuple is a constant once its is defined we can just read the items but we can not update or add or
# delete particular item
groceries = []
# CRUD => create,read,update,delete
# List => it supports all CRUD
# create
bankregistrationdetails = ("HDFC","APFJ344KHHKK","Mumbai")
# read
# we are reading with index
# index will start from 0
print(bankregistrationdetails[0])
print(bankregistrationdetails[0:2])
# update
# bankregistrationdetails[0] = 'ICICI'
# 'tuple' object does not support item assignment
# delete
# del bankregistrationdetails[0]
# 'tuple' object doesn't support item deletion
del bankregistrationdetails
# print(bankregistrationdetails)

# differences between list and tuple
# List => is mutable (changeable)
# Tuple => is immutable (unchangeable)

# List,tuple,set,dictionary
# l1= [],tuple1 =()
# set1={}
# CRUD
l1= [90,67,1,2,3,1,4,3]
print(l1)
set1 = {90,67,89,1,2,3,1,4,3,23}
print(set1)
# set will remove duplicate elements
# it is unordered
# we can't access elements based on index
# print(set1[0])
# Read
# we have to read by using for loop
# for i in set1:
#     print(i)

# update
set1.add(122)
print(set1)
set1.update([134,145])
print(set1)

# delete
# del set1
# print(set1)
set1.remove(145)
set1.discard(145)
print(set1)
# difference between remove and discard
# remove => it will directly remove the item
# discard => first it will check whether item exists or not , if exists then only it will delete
# list => mutable
# tuple => immutable
# set => mutable

# intersection,union,difference,differenceupdate,issubset,issuperset
# intersection => by using intersection we can get common elements from two sets
set1 = {1,2,3,5,6,7,8}
set2 = {1,2,66,35,33,7,8}
set3  = set1.intersection(set2)
print(set3)
set4 = set1.union(set2)
print(set4)


set6 = set2.difference(set1)
print("difference of set6" , set6)

set5 = set1.difference(set2)
print("difference",set5)
print('set1 after difference',set1)
set2.difference_update(set1)
print("set2 after difference update of",set2)


# l1 =[1,2,3,4]
# l2 =[1,2,3,45,6,7]
# l3 = l1+l2
# print(l3)
#
# l1 = [1,2,3,4,1,2,3]
# l2 = [3,4,5,34,24]
# # convert it to set
# set1 = set(l1)
# print(set1)

set7 = {1,2,3,4,5}
set8 = {1,2,3}
print(set8.issubset(set7))
print(set7.issubset(set8))

print(set7.issuperset(set8))

# list,tuple,set
l1 = []
print(type(l1))
tup1 = ()
print(type(tup1))
set1 = {1}
print(type(set1))
set2 = set()
print(set2)
set2.add(12)
set2.update([23,44])
print(set2)
print(type(set2))

l1 = [12,2,3,4,5,5,9,4,7,[4,5]]
l1[9] = [67,5]
print(l1[1:])
tupl1 = (1,2,3,[4,5])
tupl1[3] # [4,5] => list => 0 ,1
print(tupl1)

# dictionary
dict1 = {}

str1 = '6/89323233'
print(float(str1))
print(type(float(str1)))
aa = 121.23
print(str(aa))
print(type(str(aa)))




