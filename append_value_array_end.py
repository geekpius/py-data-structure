"""
    Given a list of sorted numbers, 
    insert a value of 15  at the end of the list.
    Here's an example and some starting code:

    def append(arr, value):
    # Fill this in.

    print(append([1, 2, 4, 9, 7, 10], 15))
    # [1, 2, 4, 20, 9, 7]
"""

def append(arr, value):
    """
        Create a new list with the curren list size
        Iterate current list from the start of the list
        Keep pushing element to the new list
        Insert the value at end index of the list 
    """
    arr_size = len(arr)
    new_arr = [None] * (arr_size+1)
    for i in range(arr_size):
        new_arr[i] = arr[i]
    new_arr[arr_size] = value
    return new_arr


print(append([1, 2, 4, 9, 7, 10], 15))


