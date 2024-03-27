# Write a program that takes a string as input and prints its reverse.

input_str = input()
reverse_str = ""
for i in input_str:
    reverse_str = i + reverse_str
print(reverse_str)
