'''
 Create a program that defines a variable with the same name as a global variable inside a function and observe its scope.
'''

x = 10

def my_function():
    x = 20

    print("Inside the function, x is:", x)

my_function()
print("Outside the function, x is:", x)
