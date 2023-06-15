# Justin L.
# CSC 391
# Project 1 - Quicksort Implementation 

def quicksort(arr,p,r):
    """ Funtion that performs quicksort

    Recursively calls until partition fully sorts the array

    Parameters
    ----------
    count : int
        Value increments per line being iterated through the program
    assign : int
        Increments per assignment made through the program
    p : int
        Beginning index of the array
    r : int
        Ending index of the array
    arr : list
        Array being sorted
    temp_count & temp_assign : int
        Counters to channel into our local variables - count, assign

    Returns
    ----------
    count : int
        Amount of lines executed through the program
    assign : int
        Amount of assignments executed through the program
    """
    count = 0
    assign = 0

    if p < r:

        temp_count = 0
        temp_assign = 0

        q, temp_count, temp_assign = partition(arr,p,r)

        count += temp_count
        assign += temp_assign

        temp_count, temp_assign = quicksort(arr,p,q-1)

        count += temp_count
        assign += temp_assign

        temp_count, temp_assign = quicksort(arr,q+1,r)

        count += temp_count
        assign += temp_assign


    return count, assign

def partition(arr,p,r):
    """ Partition function. 

    This function chooses the rightmost element and uses it as a pivot to compare with other elements in the array to sort to.
    It then swaps elements with which element is greater
    returns the position where partition is performed. 

    Parameters
    ----------
    count : int
        Value increments per line being iterated through the program
    assign : int
        Increments per assignment made through the program
    p : int
        Beginning index of the array
    r : int
        Ending index of the array
    arr : list
        Array being sorted

    Returns
    ----------
    count : int
        Amount of lines executed through the program
    assign : int
        Amount of assignments executed through the program
    i + 1 : int
        Next index to be sorted through
    """
    count = 0
    assign = 0

    x = arr[r] 
    assign += 1
    i = p - 1
    assign += 1
    for j in range(p,r):
        count += 1
        if arr[j] <= x:
            i = i + 1
            assign += 2

            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i+1], arr[r]) = (arr[r], arr[i+1])
    assign += 1

    return i+1, count, assign