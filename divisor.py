# Dora Jambor, dorajambor@gmail.com
# September 2015
# This is one of my exercises to MIT 6.00.1x


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)