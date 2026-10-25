class Student:
    def __init__(self,roll_no,name,marks):
        self.roll_no=roll_no
        self.name=name
        self.marks=marks
        
    def display(self):
        print(f"rollno:{self.roll_no}\t name:{self.name} \t marks:{self.marks}")
    
        
s1=Student(84,"Darshan",99)
s2=Student(21,"Amit",87)

s1.display()
s2.display()