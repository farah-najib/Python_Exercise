'''
Given a string, return a string where for every char in the original .
doubleChar('The') → 'TThhee' doubleChar('AAbb') → 'AAAAbbbb' doubleChar('Hi-There') → 'HHii--TThheerree'
'''
def double_char (text):
    result = ""


    for char in text:

        result += char * 2

    return result




print(double_char('The'))
print(double_char('AAbb'))       
print(double_char('Hi-There'))
