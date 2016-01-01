# Dora Jambor, dorajambor@gmail.com
# September 2015
# This is one of my exercises to MIT 6.00.1x


def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr == '' :
        return 0
    else:
        return 1 + lenRecur(aStr[1:])