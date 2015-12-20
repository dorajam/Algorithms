# Social Network
# Dora Jambor, dorajambor@gmail.com
# 28.11.2015

'''
Social network connectivity. 

Given a social network containing N members and a log file containing 
M timestamps at which times pairs of members formed friendships, design
an algorithm to determine the earliest time at which all members are 
connected (i.e., every member is a friend of a friend of a friend ... 
of a friend). Assume that the log file is sorted by timestamp and 
that friendship is an equivalence relation. The running time of your 
algorithm should be MlogN or better 
and use extra space proportional to N.
'''

import random, pdb

# find the root of the person
def root(index):
    while (index != IDs[index]):
        index = IDs[index]
    return index

def checkIndex(index):
    if index < 0 or index >= size:
        print 'This is an invalid index'

# boolean: True if connected
def connected(p,q):
    return root(p) == root(q)
    
def allConnected():
    return numRoots == 1
    
def union(p, q):
    checkIndex(p)
    checkIndex(q)

    pRoot = root(p)
    qRoot = root(q)
        
    global numRoots
    print numRoots
    
    # if not connected yet - not the same component
    if pRoot != qRoot:
        numRoots = numRoots - 1
        
        # weight it by sizes
        if sizes[pRoot] < sizes[qRoot]:
            IDs[pRoot] = qRoot
            sizes[qRoot] += sizes[pRoot]
        elif sizes[pRoot] > sizes[qRoot]:
            IDs[qRoot] = pRoot
            sizes[pRoot] += sizes[qRoot]
        else:
            IDs[qRoot] = pRoot
            sizes[pRoot] += sizes[qRoot]
                                  
def play(size):
    global total
    while numRoots > 1:
        p = random.randrange(0,size)
        q = random.randrange(0,size)
        print p, q
      
        if connected(p, q) == False:
            union(p, q)
            total += 1
    return total

size = 30
IDs = range(size)
numRoots = size
sizes = [1] * size
total = 0 
play(size)   
        
    
    