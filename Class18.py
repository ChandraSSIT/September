# Single level inheritance, multiple inheritance , multilevel inheritance
# Over loading  => defining same function with different signature in same class
# Over riding  => defining same function with same signature in parent and child class

class grandparent:
  def __init__(self,grandparentname):
     self.grandparentname = grandparentname

  def properties(self):
      print("grand parent properties")

class parent(grandparent):
    def __init__(self,name):
        self.parentname = name
        super().__init__("john")
        
    def properties(self):
        print("father properties")
        super().properties()

parentobj = parent("abc")
parentobj.properties()
print(parentobj.parentname)
print(parentobj.grandparentname)

class mother:
    def __init__(self,name):
        self.mothername  = name
    def properties(self):
        print("mother properties")

class child(parent,mother):
    def __init__(self,name):
        self.childname = name
        mother.__init__(self,name)
        parent.__init__(self,name)

    # over riding
    def properties(self):
        print("child properties")
        super(child, self).properties()
        mother.properties(self)
        parent.properties(self)
#
#
#
#
childobj = child('abc')
childobj.properties()
print(childobj.parentname)
childobj.mothername