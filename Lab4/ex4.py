'''
 Write a program that modifies a global variable inside a function

'''
global_variable = 10

def modify_global():
    global global_variable
    global_variable = 20


print("Initial value of global variable:", global_variable)
modify_global()
print("Modified value of global variable:", global_variable)
