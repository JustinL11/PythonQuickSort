# main.py
#
# Usage: python3 main.py filename
#
#Created Justin L. - 1/24/23
#

from quick import *
import sys
import os

sys.setrecursionlimit(1000000000)

def read_to_file(filename):
    """Reads the given filename and returns them in a list.
    
    The values are read one per line. 

    Parameters
    ----------
    the_foldername : string
        Name of the folder directory
    filename : string
        Name of the file to be read/written to
    arrleng : int
        Number of values from file
    list_of_nums : list
        List of values that is being written to and sorted

    Returns
    ----------
    list_of_nums : list
        Array of ints from the file

    """
    list_of_nums = []
    infile = open( filename, 'r')
    for aline in infile:
        anumber = int( aline)
        list_of_nums.append(anumber)
    return list_of_nums


def write_to_file(filename, list_of_nums):
    """Writes the given list of numbers out to a file given the filename.
    
    The values are written one per line.

    Parameters
    ----------
    filename : string
        Name of the file to be read/written to
    list_of_nums : list
        List of values that is being written to and sorted

    """
    outfile = open( filename, 'w')
    for value in list_of_nums :
        aline = str(value) + "\n"
        outfile.write( aline)
    outfile.close()

def main():
    """ Takes a list of values from a list, sorts them, and writes to file

    The values are written and read one per line. 
    Outputs the values before and after the quicksort. 

    Parameters
    ----------
    the_foldername : string
        Name of the folder directory
    filename : string
        Name of the file to be read/written to
    arrleng : int
        Number of values from file
    list_of_nums : list
        List of values that is being written to and sorted

    """
    
    if len(sys.argv) < 2:
        print( "Usage: python3 main.py foldername/")
        exit()
    
    the_foldername = sys.argv[1]

    #Reads the file and appends them to an array

    for filename in os.listdir(the_foldername):
        print(filename)
        if filename.endswith(".txt"):

            list_of_nums = read_to_file(f"{the_foldername}/{filename}")
            arrleng = len(list_of_nums)

            values = quicksort(list_of_nums, 0, arrleng - 1)

            print("Counts and Assignments: ", values)
                
            #Writes to file -- 
            write_to_file(f"{the_foldername}/{filename}",list_of_nums)
    
if __name__ == "__main__" :
    main()