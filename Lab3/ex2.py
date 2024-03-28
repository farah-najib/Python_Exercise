'''
Given a string, return a new string made of every other character starting with the first, so "Hello" yields "Hlo".
Example:
stringBits('Hello') → 'Hlo' stringBits('Hi') → 'H' stringBits('Heeololeo') → 'Hello'

'''
def string_bits(text) :
    result = ""
    for i in range(0, len(text), 2):
        result += text[i]

    return result


print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
