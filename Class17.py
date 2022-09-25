# Inheritance
# Parent and child relation
# where child class can access the parent class functionality and can extend
# or override the functionality

# defining same function in child class

class father:
    def get_properties(self):
        return "2 houses"
    def myhouseaddress(self):
        return "121/23/12 ATP"

class mother:
    def get_mother_properties(self):
        return "1 houses"

    def myhouseaddress(self):
        return "544-77 BLR"

class child(father,mother):

    def get_properties(self):
        return "1 shoping complex"

    def get_my_earned_properties(self):
        return  "1 plot"

class grandchild(child):
    def grand_details(self):
        print("grnad child")

parentobj = father()
print(parentobj.get_properties())


childobj = child()
print(childobj.get_properties())
print(childobj.get_mother_properties())
print(childobj.get_my_earned_properties())
print(childobj.myhouseaddress())

grandchildobj = grandchild()
grandchildobj.get_mother_properties()
grandchildobj.get_properties()
grandchildobj.myhouseaddress()
grandchildobj.grand_details()




