''' Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.
Example:
arrayCheck([1, 1, 2, 3, 1]) → True arrayCheck([1, 1, 2, 4, 1]) → False arrayCheck([1, 1, 2, 1, 2, 3]) → True '''

def array_check(integers):
    for i in range(len(integers)-2) :
        if integers[i] == 1 and  integers[i+1] == 2 and integers[i+2] == 3:
                  return True

    return False

print(array_check([1, 1, 2, 4, 1]))
print(array_check([1, 1, 2, 4, 1]))
print('The result sould be true',array_check([1, 1, 2, 1, 2, 3]))
