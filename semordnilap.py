# Dora Jambor, dorajambor@gmail.com
# September 2015
# This is one of my exercises to MIT 6.00.1x

'''
Given two strings the program returns true/false whether the word 
is identically read from both the beginning or the end - that is, the word is a semordnilap.
'''


def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if str1 == '' or str2 == '':
        return False
    
    if len(str1) == 1 and len(str2) == 1:
        if str1 == str2:
            return True
        else:
            return False
    
    if str1[0] == str2[-1] :
        return semordnilap(str1[1:],str2[0:-1])
    else: 
        return False