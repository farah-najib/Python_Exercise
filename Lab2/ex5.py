# Write a program that takes a list of integers as input and uses list comprehension to create a new list containing only the even numbers from the original list.
#I solve without using list comprehension
input_list = input("Enter a list of integers separated by spaces: ").split()
even_numbers_list = []

for i in input_list:
    num = int(i)
    if num % 2 == 0:
        even_numbers_list.append(num)

print("Original list:", input_list)
print("New list containing only even numbers:", even_numbers_list)
