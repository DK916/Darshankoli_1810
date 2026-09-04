# Q.1 Program to calculate percentage of 5 subjects

sub1 =int(input("enter a number 1:"))
sub2 = int(input("enter a number 2:"))
sub3 = int(input("enter a number 3:"))
sub4 = float(input("enter a number 4:"))
sub5 = int(input("emter a number 5:"))

totalmarks = sub1+sub2+sub3+sub4+sub5
#print(totalmarks)

percentage = (totalmarks/500)*100
print("totalmarks:",totalmarks,)
print("percentage:",percentage," % ")