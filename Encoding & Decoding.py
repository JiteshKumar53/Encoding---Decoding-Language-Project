print('Project - Crypto')
def enigma_light():

# Create key strings
     keys = 'abcdefghijklmnopqrstuvwxyz !'
# Autogenerate the values strings by offsetting original strings
     values = keys[-1] + keys[0:-1]
     #print(keys)
     #print(values)
# create two dictionaries
     dict_e = dict(zip(keys, values))
     dict_d = dict(zip(values,keys))
# OR create 1 and then flip
     #dict_e = dict(zip(values, keys))
     #dict_d = {value:keys for key, value in dict_e.items()}
     
# user input 'the message' and mode 
     msg = input('Enter your secret message: ')
     mode = input('Crypto mode: encode (e) OR decrypt as (d): ')
# run encode or decode 
     if mode.lower() == 'e':
         new_msg = ''.join ([dict_e[letter] for letter in msg.lower()])
     else: 
         new_msg = ''.join ([dict_d[letter] for letter in msg.lower()])
         
     return new_msg.capitalize()
# return result
# clean and beautify the code

print (enigma_light())
