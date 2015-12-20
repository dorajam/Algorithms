# Problem in MIT 6.00x
# Author: Dora Jambor, dorajambor@gmail.com
# September, 2015

'''
Given initial balance and a fixed monthly payment, 
the algorithm calculates the total amount paid after 12 months 
and the remaining balance with the accrued interest.

'''


balance = 3329
month = 0
r = 0.2
mr = 0.04
total = 0

for i in range(1,13):
    paid = 240
    afterMMP = balance - paid
    total += paid
    balance = afterMMP + (r/12)*afterMMP
    print 'Month: %i' %i
    print 'Minimum monthly payment: %0.2f' %paid
    print 'Remaining balance: %0.2f' %balance

print 'Total paid: %0.2f' %total
print 'Remaining balance: %0.2f'% balance