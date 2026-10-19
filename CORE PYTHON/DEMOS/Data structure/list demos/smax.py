li=[40,70,20,30,47]

max=li[0]
smax=0

for ind in range(2,len(li)):
    if(li[ind]>max):
        smax=max
        max=li[ind]
        
    elif(li[ind]>smax):
        smax=li[ind]
        
        print("max:",max)
        print("smax:",smax)