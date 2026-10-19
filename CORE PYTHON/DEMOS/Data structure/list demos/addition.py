li=[10,20,30,40,50,60,70]
#method 1:iterrating values
sum=0

# for ele in li:
#    sum+=ele
   
#    print(sum)

#mdthod 2:indexing

for ind in range(0, len(li)):
    sum+=li[ind]
print(sum)