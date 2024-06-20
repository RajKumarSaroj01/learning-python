x="""this is,
multiline 
string 
or 
sentence example"""

print(x)


# loop in string 
x="python"

for a in x:
    print(a)

# len of string 
print("len",len(x))    

x= "python is good programming language"

if "good" in x:
    print("yes it's present")

if "Good" in x:
    print("yes it's present and matching case in-sensitive")  

# concatenate string with numbers, just use the f symbol infront of text

age=19
x= f"my age is {age}"
print(x)       

x=format("my age is {age}")
print(x)