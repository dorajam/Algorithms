# Dora Jambor, dorajambor@gmail.com
# January 2016

''' 
Implements a function that returns all permutations of string s
'''
result = []

# check if string is already in the list
def isIn(string1, string2):
    if string1 in string2:
        return True
    return False

def permutation(s):
    global result
    if len(s) == 1 or len(s) == 0:
        return result.append(s)
    else:
        while isIn(s, result) == False:
            result.append(s)
            print s, result
            return permutation(s[0] + s[-1] + s[1:-1])
        while isIn(s[1:] + s[0], result) == False:
            return permutation(s[1:] + s[0])      
        
permutation('dora')