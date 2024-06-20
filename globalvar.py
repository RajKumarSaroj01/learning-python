
x="global variable"

def funPrintGlobalVar():
    print(x)

def funPrintLocalVar():
    x="local variable"
    print(x)

def funOverrideGlobalVar():
    global x
    x="Override global var"
    print(x)


funPrintGlobalVar()
funPrintLocalVar()
funOverrideGlobalVar()    