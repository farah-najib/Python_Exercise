# Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.

tuple_elements = (1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
new_tuple=()
for element in tuple_elements :
    if element%2 == 0 :
      new_tuple+=(element,)

print("new tuple:",new_tuple)
