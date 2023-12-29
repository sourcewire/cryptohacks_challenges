from pwn import *

string = "label"

def string_to_unicode(s):
    unicode_values = [ord(char) for char in s]
    return unicode_values

string_unicode_list = string_to_unicode(string)
#print(string_unicode_list)

printXor = xor(string_unicode_list, 13)
print(printXor)