# Devion Buchynsky 
# Part C - Convert the string to all uppercase if it contains at least 3 uppercase characters in the first 5 characters. 

uppercase_characters_1 = 'Hello world'
uppercase_characters_2 = 'HEllo world'
uppercase_characters_3 = 'HELlo world'
uppercase_characters_4 = 'HELLo world'
uppercase_characters_5 = 'HELLO world'

def convert_uppercase_string(string_1):
    uppercase_number = 0
    for character in string_1[:5]: #this makes sure that it only looks through 5 characters in a string
        if character.upper() == character:
            uppercase_number += 1 # this keeps iterating until it reaches the 5th character
    if uppercase_number >= 3: # if there are three uppercase characters in the first 5 characters then the string turns all uppercase
        return string_1.upper()
    return string_1

print(convert_uppercase_string(uppercase_characters_1))
print(convert_uppercase_string(uppercase_characters_2))
print(convert_uppercase_string(uppercase_characters_3))
print(convert_uppercase_string(uppercase_characters_4))
print(convert_uppercase_string(uppercase_characters_5))