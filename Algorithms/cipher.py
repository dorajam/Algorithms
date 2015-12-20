# Dora Jambor
# cipher.py
# 26.11.2014

'''
Implements an algorithm to encrypt a phrase by a shift value given by the user.
'''


# Get phrase and shift value from user
phrase = raw_input('Give me a sentence to encrypt: ')
shiftkey = input('Give me a shift value: ')

def cipher(phrase, shiftkey):

    ciphertext = ""
    for c in phrase:
        # Check for upper letters
        if c.isupper():
            ascii = ord(c)
            cipher = ((ascii - 65) + shiftkey)%26 + 65
            letter = chr(cipher)
            ciphertext = ciphertext + letter
        # Check for lower letters
        elif c.islower():
            # adjust ascii values for alhabetical values
            ascii = ord(c)
            cipher = ((ascii - 97) + shiftkey)%26 + 97
            letter = chr(cipher)
            ciphertext = ciphertext + letter
        else:
            ciphertext = ciphertext + c
            
    return ciphertext

print 'The encoded sentence is:', cipher(phrase, shiftkey)
