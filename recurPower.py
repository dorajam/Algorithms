# Dora Jambor, dorajambor@gmail.com
# September 2015
# This is one of my exercises to MIT 6.00.1x


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    return base * recurPower(base, exp-1)
