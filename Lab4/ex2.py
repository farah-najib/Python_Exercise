'''
 Write a function that takes a list of numbers and returns a list containing the squares of each number using lambda.

'''


def square_list(numbers):
    squared_numbers = [(lambda x: x ** 2)(num) for num in numbers]
    return squared_numbers

numbers = [1, 2, 3, 4, 5]
print(square_list(numbers))
