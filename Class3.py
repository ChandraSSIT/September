
# List => collection of different data type elements
bankdetails = ['chandra',12123443434,'ATP,AP,523343',2333.33,'ATP','HDFC']
# bankdetails = [firstname,12333443,completeaddress,totalamount,'HDFC']
print(bankdetails)
print(type(bankdetails))
# CRUD  => Create ,Read ,update ,delete
# Create
aadhardetails = [12233333,'John','ATP,AP','515001','12/12/1990']

# Read
print(aadhardetails)

# indexing => will start from 0 to total items count -1
# positive indexing
print(aadhardetails[1])
print(aadhardetails[2])
print(aadhardetails[4])

# negative indexing
print(aadhardetails[-4])
print(aadhardetails[-1])

# slicing => start index and end index we should consider +1 ,because it will take -1
print(aadhardetails[0:2])  # this works as aadhardetails[1:3] , as end index -1 , i.e 4-1 =>3
print(aadhardetails[3:5])
# slicing you know start index and you don't know end index
print(aadhardetails[3:])

# negative slicing
print(aadhardetails[-4:-2])
print(aadhardetails[-2:])

# slicing startindex, endindex, stepsize(by default it will be 1)
print(aadhardetails[0:5:2])
print(aadhardetails[0:5:3])
print(aadhardetails[0::3])

print(aadhardetails[-5::2])