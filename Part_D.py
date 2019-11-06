# Devion Buchynsky 
# Part D - If the string ends with a hyphen, remove it, and append the next string in the list to the current one.

hyphen_string = 'This sentence ends with a -'
hyphen_string2 = 'hyphen.'
hyphen_character = ['-']


#hyphen_string.append(hyphen_string2)
print('Before removing the hyphen and appending the next string: ' + str(hyphen_string))
print('This is the second string before appending it: ' + str(hyphen_string2))

for i in hyphen_character:
    hyphen_string = hyphen_string.replace(i, '') #removing the hyphen
    #hyphen_string.append(hyphen_string2)
    hyphen_string3 = hyphen_string + hyphen_string2 # adding two strings together
print('After removing a hyphen and appending the next string: ' +str(hyphen_string3))

