# Devion Buchynsky 
# Part A - Reverse the string if its length is a multiple of 4. 
# multiples of 4: 4,8,12,16......

multiple_of_4_string_letter = 'abcd'
multiple_of_5_string_letter = 'abcde'

print('Part A - Reverse the string if its length is a multiple of 4.')
print('Before function is ran.')
print(multiple_of_4_string_letter)
print(multiple_of_5_string_letter)

def reverse_string(string_1):
    if len(string_1) % 4 == 0: # if the string is a % of 4 then it will reverse the string, if not it will not do anything.
        return ''.join(reversed(string_1))
    return string_1
    
print('After function is ran.')
print(reverse_string(multiple_of_4_string_letter))
print(reverse_string(multiple_of_5_string_letter))
print("\n")

# Devion Buchynsky 
# Part B - Truncate the string to 5 characters if its length is a multiple of 5. 
# multiples of 5: 5,10,15,20...... 

multiple_of_5_string_number = '0123456789' # 10 characters
multiple_of_6_string_number = '012345' # 6 characters

print('Part B - Truncate the string to 5 characters if its length is a multiple of 5.')
print('Before funtion is ran.')
print(multiple_of_5_string_number)
print(multiple_of_6_string_number)

def truncate_string(string_2):
    if len(string_2) % 5 == 0: # if the string is a % of 5 then it will truncate the string to 5 characters, if not it will not do anything.
        return ''.join(string_2[0:5]) # [0:5] will only take 0-5 characters and not include the rest. 
    return string_2

print('After function is ran.')
print(truncate_string(multiple_of_5_string_number))
print(truncate_string(multiple_of_6_string_number))
print("\n")

# Devion Buchynsky 
# Part C - Convert the string to all uppercase if it contains at least 3 uppercase characters in the first 5 characters. 

uppercase_characters_1 = 'Hello world'
uppercase_characters_2 = 'HEllo world'
uppercase_characters_3 = 'HELlo world'
uppercase_characters_4 = 'HELLo world'
uppercase_characters_5 = 'HELLO world'
uppercase_characters_6 = 'HeLlO world' # the uppercase letters are not next to eachother, they are every other letter

print('Part C - Convert the string to all uppercase if it contains at least 3 uppercase characters in the first 5 characters. ')
print('Before function is ran.')
print(uppercase_characters_1)
print(uppercase_characters_2)
print(uppercase_characters_3)
print(uppercase_characters_4)
print(uppercase_characters_5)
print(uppercase_characters_6)



def convert_uppercase_string(string_3):
    uppercase_number = 0
    for character in string_3[:5]: #this makes sure that it only looks through 5 characters in a string
        if character.upper() == character:
            uppercase_number += 1 # this keeps iterating until it reaches the 5th character
    if uppercase_number >= 3: # if there are three uppercase characters in the first 5 characters then the string turns all uppercase
        return string_3.upper()
    return string_3

print('After function is ran.')
print(convert_uppercase_string(uppercase_characters_1))
print(convert_uppercase_string(uppercase_characters_2))
print(convert_uppercase_string(uppercase_characters_3))
print(convert_uppercase_string(uppercase_characters_4))
print(convert_uppercase_string(uppercase_characters_5))
print(convert_uppercase_string(uppercase_characters_6))
print("\n")


# Devion Buchynsky 
# Part D - If the string ends with a hyphen, remove it, and append the next string in the list to the current one.

hyphen_string = 'This sentence ends with a -'
hyphen_string2 = 'hyphen.'
hyphen_character = ['-']

print('Part D - If the string ends with a hyphen, remove it, and append the next string in the list to the current one.')
#hyphen_string.append(hyphen_string2)
print('Before removing the hyphen and appending the next string: ' + str(hyphen_string))

for i in hyphen_character:
    hyphen_string = hyphen_string.replace(i, '') #removing the hyphen
    #hyphen_string.append(hyphen_string2)
    hyphen_string3 = hyphen_string + hyphen_string2 # adding two strings together
print('After removing a hyphen and appending the next string: ' +str(hyphen_string3))
