tupl1 = (1,2,3,[4,5])
aa = tupl1[3][:] # [4,5] => list => 0 ,1
print(aa)
# list,tuple,set
# dictionary
l1 = ['chandra','hdfc',2332234233,23333]
# dictionary => key and value pair
dict1 = {'name':'chandra','bankname':'hdfc','accountnumber':2234344544,'balance':3233.33}
print(type(dict1))
print(dict1)
# create,read,update,delete
# in dictionary read process works based on key not based on index
print(dict1['name'])
print(dict1['accountnumber'])
print( dict1.keys() )
print(dict1.values())
print(dict1.items())

# custome1 = {'name':'chandra','bankname':'hdfc','accountnumber':2234344544,'balance':3233.33}
# custom2  = {'name':'john','bankname':'hdfc','accountnumber':2234344544,'balance':3233.33}
customers = [ {'name':'chandra','bankname':'hdfc','accountnumber':2234344544,'balance':3233.33} ,
              {'name':'john','bankname':'hdfc','accountnumber':2234344544,'balance':3233.33}  ]

aa  = [(35435,34534534,3543453434,34534534,345435345),56665,556556]

aa[0:5]

indicustomer = customers[0]
print(indicustomer)
print("----------")
print( 'my data is {0} ,{1}'.format(indicustomer['name']  ,indicustomer['accountnumber']))
print('----------------')
print(indicustomer['accountnumber'])

print(customers[0]['name'])


set1 = {'chandra', 'chandra'}
print(set1)
custome1 = {'name':'chandra','bankname':'hdfc','accountnumber':2234344544,'name':'mohan'}

print("///////////")
print(custome1)
# print(custome1['name'])
# dictionary keys can not be duplicate

# update
print("/////////Class 7 /////////")
customerdetail = {'name':'chandra','bankname':'hdfc','accountnumber':2234344544}
l1 =[1,2,3,4,5]
l1[0] = 334
print(l1)
customerdetail['name'] = 'john'
print(customerdetail)
customerdetail['balance'] = 234234
print(customerdetail)

# delete
del customerdetail['name']
print(customerdetail)

