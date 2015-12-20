# Dora Jambor
# games.py
# 5.12.2014

'''
Implements a few easy games to practice basic concepts.
'''

# player 1
def result(x,y):
        if x == y:
                return 'Players tie.'
        if x == 'rock' and y == 'paper':
                return 'Player 2 wins.'
        if x == 'rock' and y == 'scissors':
                return 'Player 1 wins.'
        if x == 'scissors' and y == 'rock':
                return 'Player 2 wins.'
        if x == 'scissors' and y == 'paper':
                return 'Player 1 wins.'
        if x == 'paper' and y == 'scissors':
                return 'Player 2 wins.'
        if x == 'paper' and y == 'rock':
                return 'Player 1 wins.'
        else:
                return 'Invalid input.'
        
# test by inserting some x and y
print result('rock','scissors')

# 2.4 writing methods
# is_divisible function
def is_divisible(x,y):
        if y != 0:
                if x % y == 0:
                        return True
                else:
                        return False
        else:
                return False

# tests for is_divisible
if is_divisible(10, 5) == True:
        print "is_divisible(10, 5) == True"
if is_divisible(18, 7) == False:
        print "is_divisible(18, 7) == False"
if is_divisible(42, 0) == False:
        print "is_divisible(42, 0) == False"

# non_equal function for !=
def non_equal(x,y):
        if x == y:
                return False
        else:
                return True

# test non_equal
print non_equal(2,3)


# 2.5 the random module
# import random function and generate random number
import random

def rand_divisible_3():
        lo = 0
        hi = 1000
        x = random.randint(lo, hi)
        print x
        if x%3 == 0:
                return True
        else:
                return False
print rand_divisible_3()

# roll dice
import random

def roll_dice(x,y):
        lo = 0
        hi = x
        for i in range (0, y):
                z = random.randint(lo, hi)
                print z
        print "That's all!"
        
roll_dice(6,3)

# 2.6cumulative

def cumulative(number_list):
    # number_list is a list of numbers
    total = []
    sum = 0
    for num in number_list:
        sum += num
        total.append(sum)

    return total

# tests for sum_all
print "cumulative of [4, 3, 6] is:", cumulative([4, 3, 6])
print "cumulative of [1, 2, 3, 4] is:", cumulative([1, 2, 3, 4])

# 2.7 additional list practice
def list_intersection(list1, list2):
        x = set(list1) & set(list2)
        print x


# tests for list_intersection
list_intersection([1, 3, 5], [5, 3, 1])               # [1, 3, 5]
list_intersection([1, 3, 6, 9], [10, 14, 3, 72, 9])   # [3, 9]
list_intersection([2, 3], [3,  3,  3,  2, 10])        # [3, 2]
list_intersection([2, 4, 6], [1, 3, 5])               # []


# 2.8 pig lating
VOWELS = ['a','e','i','o','u']

def pig_latin(word):
        head = word[0]
        if word[0] in VOWELS:
                word = word + 'hay'
                print word
        else:
                word = word[1:]
                word = word + head
                word = word + 'ay'
                print word

pig_latin('word')
pig_latin('ord')


# 2.11

NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank',
         'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']

AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]

def people():
        d = dict()
        dict = {'Alice' : 20,'Bob':21, 'Cathy':18, 'Dan':18, 'Ed':19, 'Frank':20,
         'Gary':20, 'Helen':19, 'Irene':19, 'Jack':19, 'Kelly':22, 'Larry':19}
        for i in AGES:
                if i not in dict:
                        print "Noone has this age"
                else:
                        return dict
        

print 'Dan' in people(18) and 'Cathy' in people(18)
print 'Ed' in people(19) and 'Helen' in people(19) and \
      'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19)
print 'Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20)

print people(21) == ['Bob']
print people(22) == ['Kelly']
print people(23) == []
