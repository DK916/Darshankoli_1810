def linear_search(li,search_ele):
    
    size=len(li)
    for ind in range(0,size):
        if (li[ind]==search_ele):
            return ind
        
        else:
            return -1
li=[40,50,30,20,10,60]
ele=20
res=linear_search(li,ele)
if(res!=-1):
            
    
     print(f'{ele} is present at index {res}.')
else:
     print(f'is not present in index')