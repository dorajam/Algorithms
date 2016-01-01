# Dora Jambor, dorajambor@gmail.com
# September 2015
# This is one of my exercises to MIT 6.00.1x


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    x = min(a,b)
    z = min(a,b)
    y = max(a,b)
    
    while y % x != 0 or z % x != 0:
        x -= 1
    return x
    