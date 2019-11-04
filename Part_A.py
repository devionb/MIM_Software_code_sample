# Devion Buchynsky 
# Part A - Reverse the string if its length is a multiple of 4. 
# multiples of 4: 4,8,12,16......


def reverse_string(string_1):
    if len(string_1) % 4 == 0: # if the string is a % of 4 then it will reverse the string, if not it will not do anything.
        return ''.join(reversed(string_1))
    return string_1

print(reverse_string('abcd'))
print(reverse_string('abcde'))

