class Employee:
    def __init__(self,id, name,sal):
        self.id__=id
        self.name__=name
        self.sal__=sal
        
    
    def getid(self):
        return self.__id
    def setid(self,nid):
        self.id__=nid
        
    def __str (self):
        return f"id={self.__id}Name={self.__name}Sal={self.sal}"
e1=Employee(102,"darshan",3000)
print(e1.getname())
e1.setsal(7000)
print(e1)

# class HR(Employee):
#     def __str__(self):
#         print(self._id)
#         return super().__str__()
#     e1=Emp(12,"Swaraj",1234)
#     print(e1.getid())
#     e1.setid(19)
    
# print(e1.get)