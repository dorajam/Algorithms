# Problem in MIT 6.00x
# Author: Dora Jambor, dorajambor@gmail.com
# September, 2015

'''
In this problem, you are asked to find the amount of radiation a person 
is exposed to during some period of time. There is a function f that will be 
defined for you that you can call from within your function that 
describes the radioactive decay curve for the problem.
'''

# Given function for radioactive decay
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

# Function implemented
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    total = 0
    start = float(start)
    stop = float(stop)
    while start < stop:
        total = total + f(start) * step
        start = start + step
    if start == stop:
        return total
    if start > stop:
        start = start - step
        total = total - f(start) * step
        incr = stop-start
        total += f(start) * incr
        return total
        
