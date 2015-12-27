# Problem in MIT 6.00x
# Author: Dora Jambor, dorajambor@gmail.com
# September, 2015

'''
Given initial balance, interest rate and a year period to pay it all off,
the algorithm calculates the lowest payment needed to meet 
the 12-month payback time.
Implemented using binary search
'''


balance = 3329
annualInterestRate = 0.2
total = 0

minpay = balance/12.0
maxpay = balance*((1+annualInterestRate/12.0)**12)/12.0

while True:
    b = balance
    guess = 0.5*(minpay+maxpay)   
    # checked if all paid off
    for i in range(12):
        b = (b-guess)*(1+annualInterestRate/12)    
    if b < 0:
        if abs(guess-maxpay) > 0.01:
            maxpay = guess
        else:
            break
    elif b==0: 
        break
    else:
        minpay = guess

print "Lowest Payment: %0.2f" %(guess)