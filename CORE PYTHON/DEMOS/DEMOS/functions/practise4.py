# def multiplication(a,b):
#   mul=a*b
    
#   return mul
    
# a=int(input("Enter number 1:"))
# b=int(input("Enter number 2:"))
    
# res = multiplication(a,b)
    
# print(f'multiplication is {res}')





# def subtraction(x,y):
#     sub=x-y
#     return sub

# x=int(input("Enter number 1:"))
# y=int(input("Enter number 2:"))
# res =subtraction(x,y)
# print("subtraction is :",res)

# def division(num1,num2):
#     div=num1/num2
#     return div
# num1=int(input("Enter number 1:"))
# num2=int(input("Enter number2:"))
# res=division(num1,num2)
# print("division is:",res)

def number(num1):
    sum=num1%2==0
    return sum
num1=int(input("Enter number:"))
res=number(num1)
print("number is:",res)