# abstraction ,encapsulation

class empdetails:
    firstname = ''
    lastname = ''
    surname = ''
    midlename = ''
    age =''
    address = ''
    pincode =''
    permanentaddress =''
    presentaddress = ''

from multipledispatch import dispatch
class employee:

    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.__employeedetails = []

    def __createemployee(self, name, id):
        emp = {"name": name, "id": id}
        self.__employeedetails.append(emp)

    def create_employee(self, name, id):
        self.__createemployee(name, id)

    def get_employee_detail(self):
        return self.__employeedetails

    def mydetals(self,emp):
        print(emp.firstname)
        print(emp.lastname)

    @dispatch(int,int)
    def add(self, a, b):
        print(a + b)

    @dispatch(int,int,int)
    def add(self, a, b, c):
        print(a + b + c)

    # @dispatch([])
    # def add(self,*args):
    #     sum =0
    #     for i in args:
    #         sum +=i
    #     print(sum)


# abstraction
# exposing the functionality to outside world by hiding the implementation
emp = employee('chandra', '2332')
emp.create_employee('chandra', '1232')

# encapsulation
# it will hide the members and member functions by making them as private , in python __ indicates private

# polymorphism
# defining a function with same name with different signature
# over loading  (i.e defining a function with same name with different signature in same class)
# python by default it will not support over loading . because it uses MRO i.e method resolution order
emp.add(2, 3)
emp.add(2,3,4)

empdetailobj = empdetails()
empdetailobj.firstname ='abc'
empdetailobj.lastname ='efg'

emp.mydetals(empdetailobj)
# def add(a,b):
#     return a+b

# def add(**args):
#     sum = 0
#     for i in args.values():
#         sum +=i
#     return sum
#
#
# print(add(a=2,b=3,c=4))
# print(add(x=3,y=4,m=5,z=6,n=7))

# *args,**kwargs


# class , object ,abstraction ,encapsulation ,polymorphism (over loading, over riding) ,inheritance