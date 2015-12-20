# Dora Jambor
# chef.py
# 5.12.2014

'''
Implements an easy automated order confirmation.
'''

# Chefs menu
# Display menu
A = '1. Soup and salad'
print A
B = '2. Pasta with meat sauce'
print B
C = '3. Chefs special'
print C

# Take order
prompt = 'Which number would you like to order? '
order = input(prompt)

# Answer
A = 'Soup and salad'
B = 'Pasta with meat sauce'
C = 'Chefs special'

if order == 1:
    print 'One', A, 'coming right up!'
if order == 2:
    print 'One', B, 'coming right up!'
if order == 3:
    print 'One', C, 'coming right up!'
elif order > 3 or order < 1:
    print 'Sorry, that is not a valid choice.'


