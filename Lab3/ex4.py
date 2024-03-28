'''
Return the number of even integers in the given array/list.
 Examples:
 count_evens([2, 1, 2, 3, 4]) → 3
 count_evens([2, 2, 0]) → 3 count_evens([1, 3, 5]) → 0

'''
def count_evens(integers):
    even_count = 0
    
    for num in integers:

        if num % 2 == 0:
            even_count += 1

    return even_count


print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
