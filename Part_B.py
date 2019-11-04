# Devion Buchynsky 
# Part B - Truncate the string to 5 characters if its length is a multiple of 5. 
# multiples of 5: 5,10,15,20...... 

multiple_of_5_string = '0123456789' # 10 characters
multiple_of_6_string = '012345' # 6 characters

def truncate_string(string_1):
    if len(string_1) % 5 == 0: # if the string is a % of 5 then it will truncate the string to 5 characters, if not it will not do anything.
        return ''.join(string_1[0:5]) # [0:5] will only take 0-5 characters and not include the rest. 
    return string_1

print(truncate_string(multiple_of_5_string))
print(truncate_string(multiple_of_6_string))