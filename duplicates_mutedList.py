# Dora Jambor
# January 2016
# Returns same list without duplicates

lst = ['a','b','c','a','b', 'a']

def duplicate(here):
    if len(here) <= 1:
        print 'No duplicates found'
        
    if len(here) == 2:
        if here[0] == here[1]:
            return [here[0]]
    
    s = here
    for i in range(len(here)-2):
        j = i + 1
        print i, j
        
        while j < len(s):
            print j
            if s[i] == s[j]:
                print s
                del s[j]
                print s
            else:
                j += 1
    return s
            
            
print duplicate(['d','d'])