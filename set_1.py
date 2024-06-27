# unordered : elt do not any particular order int the set 
# unchanageable : one can not modify the elt inserted, but can be removed , also more elt can be in the set 
# duplicate not allowed :


set1= {1,2,3,4}
print(set1)
print(type(set1))

for x in set1:
    print(x)

# add a elt in set 
set1.add(5)
print(set1)

# remove elt in set 
set1.pop()
print(set1)
# remove the particular elt from the set 
set1.remove(2)
print(set1)

# merge the two sets 
set2={"e1","e2"}
set1.update(set2)
print(set1)