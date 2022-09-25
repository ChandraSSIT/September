class employee:
    name ='csds'
    firstname ='chandra'
    # constructor
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.employeedetails =[]

    def __str__(self):
       return "chandra"

    def create_employee(self,name,id):
        emp = {"name":name,"id":id}
        self.employeedetails.append(emp)

    def get_employee_detail(self):
        return self.employeedetails

    def get_employee(self,id):
        print(self.get_employee_department('ECE'))
        print(self.get_my_details('BLR'))
        for i in self.employeedetails:
            if i['id'] == id:
                return i



    @staticmethod
    def get_employee_department(dep):
        return dep

    @classmethod
    def get_my_details(cls,address):
        print(cls.firstname , address)
        return cls.get_employee_department('IT')



# constructor => while constructing an object this constructor will call first
obj = employee('123', 'abc')
obj.create_employee('chandra','3333')
obj.create_employee('akbar','123213')
obj.create_employee('latha','233434')
print(obj.get_employee_detail())
print(obj.get_employee('3333'))

# methods types => instance methods , class methods,static methods
# Instance methods => the methods which will access with object is called instance methods

obj.get_employee_detail()

# static method => access method without creating object , by directly mentioning class name
print(employee.get_employee_department('IT'))

# class method => access method without using object and inside method we can access class members
# and static methods inside class method
print(employee.get_my_details('ATP'))
print(obj.get_my_details('ATP'))




