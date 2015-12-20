# Dora Jambor
# population.py
# 5.12.2014

'''
Reads data from csv file and turns it into dictionary, 
calculates the growth rate as a new dictionary, then plots it on a graph.
'''

# Display data from csv file
def print_population_list(filename):
    '''
    Prints the population read from a CSV file, containing 
    years in column 2 and population / 1000 in column 3.

    @param filename: the filename to read the data from
    '''
     
    # Import module
    import csv
    
    # open file for reading
    file = csv.reader(open(filename))

    # skip the header of the file
    next(file, None)
        
    # print the formatted data from the file
    for line in file:
        print line[2] + ': ' + str(int(float(line[3]) * 1000))

# Display data from csv file by creating dictionary
def population_dict(filename):
    """
    Reads the population from a CSV file, containing 
    years in column 2 and population / 1000 in column 3.

    @param filename: the filename to read the data from
    @return dictionary containing year -> population
    """

    # Import module
    import csv
    
    # open file for reading
    file = csv.reader(open(filename))

    # skip the header of the file
    next(file, None)
        
    for line in file:
        mydict = {int(line[2]):int(float(line[3])*1000) for line in file}
    return mydict

def growth():
    '''
    Takes the dictionary created from population.csv as an element,
    calculates growth rates over the population then creates and returns
    a new dictionary.
    '''
    
    mydict = population_dict('population.csv')
    years = mydict.keys()
    population = mydict.values()

    growth_rates = []
    for i in range(0, len(population)-1):
        rate = (float(population[i+1]) - float(population[i]))/float(population[i])*100
        rate = "%.2f" % rate
        growth_rates.append(rate)
    growth_dict = dict(zip(years, growth_rates))
    return growth_dict

def graph():
    import matplotlib.pyplot as plt
    import numpy as np

    growth_dict = growth()
    
    plt.plot(growth_dict.keys(), growth_dict.values(), 'bo')
    plt.xlabel('Years')
    plt.ylabel('Growth Rate in percentage')
    plt.title('Population growth per year')
    plt.grid(True)
    plt.show()
    
# run the functions
print_population_list('population.csv')
print population_dict('population.csv')
graph()

