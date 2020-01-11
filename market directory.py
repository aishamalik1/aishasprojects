"""
#aishamalik
#am5080
"""

from collections import defaultdict

fmarket = defaultdict(list)
towntozip = defaultdict(set)
def read_markets(filename):
    """
    Read in the farmers market data from the file named filename and return 
    a tuple of two objects:
    1) A dictionary mapping zip codes to lists of farmers market tuples.
    2) A dictionary mapping towns to sets of zip codes.
    """
    f = open(filename,'r')
    for line in f:
        line = tuple(line.split('#'))
        zipcodes = line[4]
        fmname = (line[1], line[2], line [3], line[0], zipcodes)
        town = line[3].lower()
        fmarket[zipcodes].append(fmname)
        towntozip[town].add(zipcodes)
    return fmarket, towntozip
    
def print_market(market):
        """
        Returns a human-readable string representing the farmers market tuple
        passed to the market parameter.
        """
        final = '{} \n{} \n{} {} {}'.format(market[0], market[1], market[2], market[3], market[4])
        return final
        
if __name__ == "__main__":        
        
    try:
        read_markets('markets.txt')
        user = input("Enter a zipcode, town name or quit. ")
        while user != 'quit':
                if user.isdigit():
                    if user in fmarket:
                        for mkts in fmarket[user]:
                            print(print_market(mkts))
                    else:
                        print("No market found :(")
                else:
                    if user in towntozip:
                        for town in towntozip[user]:
                            for zippy in towntozip[user]:
                                print(print_market(zippy))
                    else:
                        print("No market found :(")
                user = input("Enter a zipcode, town name or quit. ")
                    
    except (FileNotFoundError, IOError): 
        print("Error reading {}".format("market.txt"))    