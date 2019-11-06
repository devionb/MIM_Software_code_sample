# Devion Buchynsky 
# Part A - Reverse the string if its length is a multiple of 4. 
# multiples of 4: 4,8,12,16......

multiple_of_4_string_letter = 'abcd'
multiple_of_5_string_letter = 'abcde'

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

