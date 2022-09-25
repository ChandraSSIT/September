firstname ='chandra'
address ='ATP,AP'
pincode = '515001'

# string concatenation
completeaddress = firstname.capitalize() +'\n' + address+'\n' + pincode
print(completeaddress)
print(type(completeaddress))

prinicipalamount = 2333  # int
intrest = 223.78 # float
totalamount = prinicipalamount + intrest
print(totalamount)
print(type(totalamount))

# data type conversion
# converting from one data type to other
# Explict ,Implicit data type conversions
# Implicit data type conversion
#  it's automatically convert from one type to other type , it converts to the higher data type
# in below it converts integer to float

prinicipalamount = 2333  # int  2333.00 + 223.78
intrest = 223.78 # float
totalamount = prinicipalamount + intrest

# Explicit data type conversion
# we manually change the data type
totalamount = prinicipalamount + int(intrest)
print(totalamount)
print(type(totalamount))


firstname ='chandra'
address ='ATP,AP'
pincode = 515001
isexistsincountry = True

completeaddress = firstname.capitalize() +'\n' + address+'\n' + str(pincode) + str(isexistsincountry)
print(completeaddress)

# Implicit,Explict

# Primitive data types => string,float,int,bool
# sequence of data types => its combination of data or collection of data
# List, tuple , dictionary , set

# List => collection of different data type elements
bankdetails = ['chandra',12123443434,'ATP,AP,523343',2333.33,'ATP','HDFC']
# bankdetails = [firstname,12333443,completeaddress,totalamount,'HDFC']
print(bankdetails)
print(type(bankdetails))
# CRUD  => Create ,Read ,update ,delete