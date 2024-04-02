'''
 Create a program that defines a function within another function and access variables from the outer function.
 (Often called Enclosing Scope)

'''
def outer_function():
    x = 10

    def inner_function():
        print("Accessing variable 'x' from outer function:", x)
    inner_function()
outer_function()
