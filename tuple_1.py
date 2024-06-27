

# tuple is basically unchangeable list
tuple1=(1,2,3,4)
print(tuple1)
print(type(tuple1))

t1=(1)
t2=(1,)
print("not tuple",type(t1))
print("one elt with commo is tuple",type(t2))
 
# unpack tuple  
t1=(1,2,3)
x,y,z=t1
print(x)

# unpack tuple with less number of variable, in this case one of the variabl hold remaining elt  
t1=(1,2,3,4)
x,y,*z=t1
print(z)

# multiple tuple , means copy same content again starting from the end of tuple 
t2=t1*2 
print(t2)