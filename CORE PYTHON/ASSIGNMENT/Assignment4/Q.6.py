# Q .6WAP to check if a given number is prime number or not.
n=int(input("Enter n:"))
count =0
i=1
while i<= n:
    if n % i==0:
     count+=1
    i+=1
    
if(count==2):
        print("prime number")
        
else:
        print("this is not prime number")