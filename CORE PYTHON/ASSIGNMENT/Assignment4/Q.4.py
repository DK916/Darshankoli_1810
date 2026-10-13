# 4. WAP to print factorial of a number .

n=int(input("Enter a number:"))
i=1
sum=1
while(i<=n):
    sum=sum*i
    i+=1
    
print("sum of factorial:",sum)