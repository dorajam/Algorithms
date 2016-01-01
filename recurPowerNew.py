# Dora Jambor, dorajambor@gmail.com
# September 2015
# This is one of my exercises to MIT 6.00.1x


def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    if exp%2 == 0:
        return recurPowerNew(base * base, exp/2)
    if exp%2 !=0:
        return base * recurPowerNew(base, exp-1)