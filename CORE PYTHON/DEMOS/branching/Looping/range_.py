# # # # # for i in range(2,21,2):
# # # # #     print(i)

# # # # num =5
# # # # for i in range (5,51,5):
# # # #     print(i)

# # # n =int(input("Enter a number:"))
# # # for i in range(n, n*10+1, n):
# # #     print(i)

# # # for i in range (20 ,1,-2):
# # #    print(i)
# # n=2
# # for i in range(n*10,n-1, -n):
# #     print(i)
    
# for i in range(5):
#     print(i)

num = int(input("how many fibonacci numbers you want"))
a = -1
b = 1

for i in range(num):
    c = a+b
    print(c,end='')
    a =b
    b=c