# Author: Dora Jambor, dorajambor@gmail.com
# population.py
# 5.12.2014

'''
Reads data from csv file and turns it into dictionary.
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

print_population_list('population.csv')

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

print population_dict('population.csv')



