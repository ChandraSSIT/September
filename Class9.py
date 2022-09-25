# Loops
# for while
l1 = [1, 2, 3, 4, 5, '']
for item in l1:
    print(item)

dict1 = {'name': 'chandra', 'id': 1234}
for item in dict1.items():
    print(item)

# while loops => this works with condition

count = 1
while count < 10:  # condition until condition become false it will execute
    print(count)
    count += 1

# range ,it will give range of numbers
print(list(range(0,10)))
print(list(range(0,10,2)))
print(list(range(10,-1,-1)))
print(list(range(-1,-10,-1)))

# 9 8 7 6  5 4 3 2 1 0
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14


for i in range(10): # range(0,10) => range(10)
    print(i,end=" ")

print("")
print(10)


# i want to print first 20 even numbers
# number%2 == 0

for i in range(20):
    if i%2 == 0:
        print(i)


evencount = 0
number = 0
while evencount < 21 :
      if number%2 == 0 :
          print(number,end=" ")
          evencount+=1

      number += 1

print("")
# 2 3 5 7 11
#  print first 10 prime numbers


# break => when ever condition matches it will break the loop
# continue  => next statement after the continue will not execute but it will go next iteration
for num in range(0,30):
    if num >=2 :
        if num == 2:
            print(num)
        else:
            isprimenumber = True

            for j in range(2,num):# endindex will consider as endindex-1 , if 3 it will take till 2
                if num % j == 0:  # 4 %2 = 0 ,4%3  =1 , 5 , 5%2 == 2 , 5%3 == 1 ,5%4 == 1
                    isprimenumber=False  # 4 ,
                    break


            if isprimenumber:
                print(num)


# 0 to 30
# first 50












