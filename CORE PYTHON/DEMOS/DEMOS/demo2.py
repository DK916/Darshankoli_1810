###Numeric
#1.int
var =10

#2.float
var =3.14

#3.Complex
var = 10+5j   #real +imaginary

#4.str
var="Firstbit solutions"
var ='Firstbit solutions'
var= """
This is first line
this is second line"""

var='''
this is first line
this is second line'''


#Sequential
#1.list
var =[10,20,30,40]


#2.tuple
var= (10,20,30,40)


#3.range
var=range(1,20)


###set type
#1.set
var ={10,20,30,40,50}


#2.frozenset
var = frozenset({10,20,30,40,50})
print(type(var))

###mapping
#1.dict
var ={1:'python',2:'Java',3:'c'}
print(type(var))

###Other
#1.bool
var =True
print(type(var))

#None:type
var =None
print(type(var))