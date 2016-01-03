# Dora Jambor
# January 2016
# returns copy of list without duplicates


def duplicate(li):
    seen = []
    for e in li:
        if e not in seen:
            seen.append(e)
        else:
            pass

    print seen
            
lst = ['a','b','c','a','a','a']
duplicate(lst)