print("hello")
# print("Hi")
# comment => to give explanation about the code
# identifier is unique name
# variable => its stores data in memory

# primitive data types
firstname = 'chandra' # string
print(firstname)
print( type(firstname) )
print(firstname.capitalize())
print(firstname.upper())
print(firstname.lower())

accountnumber = 1233 +111 # int (i.e integer)
print(type(accountnumber))
bankbanalance = 3243.44 #float (i.e float/decimal)
print(type(bankbanalance))
isaccountactive = True  # boolean (i.e boolean)
print(type(isaccountactive))

# data type conversion

# Implicit data type conversion
principalamount = 10000
intrest = 233.33
total = principalamount + int(intrest)
print(total)
print(type(total))
# Explicit conversion
address= '12/33,Ramnagar'
pincode = 533333
completeaddress = address+ str(pincode) # '533333'
print(completeaddress)
print(type(completeaddress))

# set of data
# sequence data type
# its a combination of different data types
# list,tuple,set,dictionary
# CRUD operations
# Create
# Read
# update
# delete

# list
# create
groceries= ['salt','sugar','dal','vegetables','fruits','soaps'] # creating data
bankdetail =[121323,'chandra','ATP',1232.33]
print(type(bankdetail))
# read
print(groceries)
print(bankdetail)
# indexing
print(bankdetail[1])
print(bankdetail[3])
print(groceries[-1])
print(groceries[-4])
# slicing
# start index ,end index ,step size
# [startindex:endindex:stepsize]
# endindex will always consider provided index-1
# step size => by default value will be 1
print(bankdetail[0:2:1])
print(bankdetail[0:4:3])

# update , add new item
laptops = ['dell','hp']
# append,extend
laptops.append('lenovo')  # with append we can add only one item
laptops.append([12,23])
print(laptops)
laptops.extend(['accer','apple']) # to add multiple items
print(laptops)

laptops[0] = 'dell inspra'
print(laptops)
laptops[1:3] = ['hp latest','lenovo i5']
print(laptops)

# delete
del laptops[4]
print(laptops)

del laptops[2:4]
print(laptops)

# it will delete completely from memory
# del laptops
# print(laptops)







