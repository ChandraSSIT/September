class mother:
    def __init__(self, name):
        self.mothername = name

    def properties(self):
        print("Mother properties")


class father:

    def __int__(self):
        pass

    def __init__(self, name):
        self.fathername = name

    def properties(self):
        print("father properties")


class child(father, mother):
    def __init__(self, name):
        self.childname = name
        super(child, self).__init__("mikey")
        mother.__init__(self, "Yan")

    def properties(self):
        print("child properties")
        super().properties()
        mother.properties(self)


childoj = child("john")
childoj.properties()
print(childoj.mothername)
print(childoj.fathername)
print(childoj.childname)
print(child.__mro__)
print(child.__bases__)


# Single , Multiple ,Multi level inheritance

# what is the base class for all the classes => object
# class , object ,abstraction , encapsulation ,polymorphism ,inheritance
# self,__init_,super()
# MRO

# issuper
# issub

class test:
    pass

print(isinstance(childoj,child))
print(isinstance(childoj,mother))
print(isinstance(childoj,father))
print(isinstance(childoj,test))

print(issubclass(father,child))

# exception handling(try and except),file operations , regex , datetime function ,

