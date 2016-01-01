# Dora Jambor, dorajambor@gmail.com
# September 2015
# This is one of my exercises to MIT 6.00.1x

'''
Checks whether the string contains the char using recursion.
'''


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    assert type(aStr) == str

    if aStr == '':
        return False
        
    if len(aStr) == 1 and aStr != char:    
        return False
    
    check = aStr[int(len(aStr)/2)]
    if char == check:
        return True
    elif char < check:
        return isIn(char, aStr[0:int(len(aStr)/2)])
    elif char > check:
        return isIn(char, aStr[int(len(aStr)/2):])
    if len(aStr) == 1 and aStr != char:    
        return False
