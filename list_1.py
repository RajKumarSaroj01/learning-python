listvar=["a","b","c","d"]

print("len is ",len(listvar))

# list with multi data type 

multiDataType=["a",1,"b",91.5,True]
for x in multiDataType:
    print(x)

print(multiDataType[1:4])    

# inset in list 

listvar[0]="z"
print(listvar)

# update tht list with range 
# 1. give same number of elt to insert 
listvar[0:1]=["add"]
print(listvar)
# 2. give more elt, first it will replace and then add the elt and shift the remaining one 
listvar[2:3]=["insert1","insert2","insert3","insert4"]
print(listvar)
# 3. give less number of elt,  
listvar[0:3]=["insert5"]
print(listvar)

# append at the end 
listvar.append("appended")
print(listvar)

# insert at any index
listvar.insert(1,"inserted")
print(listvar)

# append list at the end 
list2=["x","y","z"]
listvar.extend(list2)
print(listvar)

# list comprehension: shortest way to create new list based on existing one
newlist=[x for x in listvar]
print("newlist ",newlist)

newlist=[x for x in listvar if "z" in x]
print("newlist ",newlist)

newlist=[x.upper() for x in listvar]
print("newlist ",newlist)

# sort the list
listvar.sort()
print(listvar)

# join two list 
list1=[1,2,3]
list2=["x","y","z"]
list3=list1+list2
print(list3)