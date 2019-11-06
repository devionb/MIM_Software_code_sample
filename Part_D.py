# Devion Buchynsky 
# Part D - If the string ends with a hyphen, remove it, and append the next string in the list to the current one.

hyphen_string = 'This sentence ends with a -'
hyphen_string2 = ' hyphen.'
hyphen_character = ['-']
newlist = ''



#hyphen_string.append(hyphen_string2)
#print(hyphen_string)

for i in hyphen_character:
    hyphen_string = hyphen_string.replace(i, '')
print('Result is: ' +str(hyphen_string))

def remove_hyphen(hyphen_string):
    for i in hyphen_string:
        #if hyphen_character == hyphen_string.endswith('-'):
            #hyphen_string = hyphen_string.replace('-', '')
            #newlist.append(i.replace('-',''))
            #hyphen_string.append(hyphen_string2)
            print(hyphen_string)
      
        

#print(remove_hyphen(hyphen_string))
#print(remove_hyphen(hyphen_string2))
