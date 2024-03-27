# Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the value from the second dictionary should be used.

dictionary1 = {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 6}
dictionary2 = {'b': 7,'f': 8, 'g': 9, 'h': 10}
merged_dictionary=dictionary1
for key, value in dictionary2.items():
    merged_dictionary[key] = value
print(dictionary1)
print(dictionary2)
print(merged_dictionary)
