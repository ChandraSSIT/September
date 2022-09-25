# OOPS (Object oriented programming structure)
# Code re usability , memory management ,scalability

# Class,object,abstraction ,encapsulation ,polymorphism ,inheritance

# Class
# Class is an entity or it's a container
# it contains members(variables) , methods (member functions)
# how to define the class


# what is function and what is method
name = 'chandra'
father_name = 'abc'
mother_name = 'abc'

def get_employee_detail1():
    return name + father_name + mother_name

get_employee_detail1()

# pep8 standards

class employee:
    name = 'chandra'
    father_name = 'abc'
    mother_name = 'abc'

    def get_employee_detail(self):
        return self.name + self.father_name + self.mother_name


# self => it represents current instance of class , by using this we can access the members and methods
# inside class




# object => it's an instance of class
x = 5
emp = employee()
print(emp.name)
emp.name ='mohan'
print(emp.father_name)
print(emp.mother_name)
emp.get_employee_detail()

emp2 = employee()
emp2.get_employee_detail()
# instance method => method which is accessed through object/instance

