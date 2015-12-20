# Author: Dora Jambor, dorajambor@gmail.com
# pyplot.py
# 5.12.2014

'''
Reads data from csv file, turns it into a dictionary,
then plots it on a graph.
'''

# Declare function to get the dictionary of the csv file
def population_dict(filename):
    # Import module
    import csv
    
    # open file for reading
    file = csv.reader(open(filename))

    # skip the header of the file
    next(file, None)
        
    for line in file:
        mydict = {int(line[2]):int(float(line[3])*1000) for line in file}
    return mydict

# Plot the dictionary onto a graph

def graph():
    # import library
    import matplotlib.pyplot as plt
    import numpy as np
    
    # create dictionary of csv file
    mydict = population_dict('population.csv')

    # create lists from dictionary for years and population
    years = mydict.keys()
    population = mydict.values()

    #plot data
    plt.plot([years], [population], 'bo')

    # labels and titles
    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.title('Population per year')
    plt.grid(True)
    plt.show()


graph()

