numbers=[10,20,30,40,50,60,70]
max= numbers[0]

for ind in range(1,len(numbers)):
    if(numbers[ind]>max):
        max=numbers[ind]
        
print("maximum nummbers:",max)  