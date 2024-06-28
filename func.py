# function in python

def fun():
    print("simple function")

fun()

# function with argument and call it by positional argumants and keyword arguments 
def fun1(x,y):
    print("x ",x)
    print("y", y)

fun1(1,2)
fun1(y=3,x=4)

# function with variable positional arguments  
def fun2(*x):
    print("1st arg",x[0])
    print("2nd arg",x[1])

fun2(2,3)    

# function with variable keyword arguments 
def fun3(**kwarg):
    print("1st arg",kwarg["x"])
    print("1st arg",kwarg["y"])

fun3(x=10,y=20)