# Problem in MIT 6.00x
# Author: Dora Jambor, dorajambor@gmail.com
# September, 2015

'''
Given string s, find the longest substring that's in an alphabetical order.
'''

s = 'wxyppdefabc'
ABC = 'abcdefghijklmnopqrstuvwxyz'
longest = s[0]
test = s[0]

for i in range(1,len(s)):
    if ABC.index(s[i-1]) <= ABC.index(s[i]):
        test += s[i]
        if len(test) > len(longest):
            longest = test
    else:
        test = s[i]

print 'Longest substring in alphabetical order is:', longest