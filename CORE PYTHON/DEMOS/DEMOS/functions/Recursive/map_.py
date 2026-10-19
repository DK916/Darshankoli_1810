data= [1,2,3,4,5,7,8,9,10]
def square (n):
    return n*n
res=list(map(square,data))
print(res)



#method2

res=list(map(lambda n:n*n,data))
print(res)