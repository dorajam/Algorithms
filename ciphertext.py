# Dora Jambor, dorajambor@gmail.com
# 01.01.2016
# Part of the cipher exercise on MIT 6.00.1x

'''
Implements a program to encrypt plaintext into ciphertext using the Caesar cipher;
returns dictionary with the plaintext and ciphertext characters
'''

import string
lower = string.ascii_lowercase
shifted_lower = []
upper = string.ascii_uppercase
shifted_upper = []
d = {}

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    for i in lower:
        shifted_lower.append((ord(i) - 97 + shift)%26 + 97)
                    
    for i in range(26):
        shifted_lower[i] = chr(shifted_lower[i])
                            
    for i in upper:
        shifted_upper.append((ord(i) - 65 + shift)%26 + 65)
        
    for i in range(26):
        shifted_upper[i] = chr(shifted_upper[i])
            
    global d     
    d = dict(zip(list(lower),list(shifted_lower)) + zip(list(upper), list(shifted_upper)))
    
    return d
    
buildCoder(23)