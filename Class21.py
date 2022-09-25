# File Operations

# Modes of file
# Read => it will read data from file
# Write => it will override existing data (means it will clear existing data) and adds new data
# append => it appends the data to existing file

file1 = open("sample.txt", 'w')
file1.write("Hi Hello how are you")
file1.close()

file1 = open("sample.txt", 'a')
file1.write("\n I am doing good")
file1.close()

file2 = open("sample.txt", 'r')
data = file2.read()
print(data)
file2.close()
# data1 = file2.readlines()
# print(data1)
# file2.close()

# context management => after execution of code inside block , objects will dispose automatically once out
# of block
with open("sample.txt", 'w+') as file3:
    file3.write("New data i am from ATP")
    file3.seek(0)  # return to the top of the file before reading, otherwise you'll just read an empty string
    abc = file3.read()
    print(abc)

# Data time functions
import datetime

dateobj = datetime.datetime.now()
print(dateobj)
print(datetime.datetime.date(dateobj))
print(dateobj.year)
print(dateobj.month)
print(dateobj.day)
print(dateobj.isoweekday())
print(dateobj.time())

import re

# re => regular expression
str1 = ' hello my ip 10.23.123.12 and connected to server ip 23.23.23.35 from 2354.67.35.345'

pattern1 = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')

print(re.findall(pattern1, str1))

# Python Identifiers,Variables,Datatypes,operators,flow controls,functions , oops,exception handling
# datetime , reg ex

dict1 = {"name": "chandra", 123: "abc", "balance": 2332.324}
dict1['bankname'] ="icici"
dict1['name'] ='icici'
print(dict1)
print(dict1[123])