"""
    Given a list of sorted numbers, 
    insert a value of 20 into the list at position 3.
    Here's an example and some starting code:

    def insert_value(arr, index, value):
    # Fill this in.

    print(insert_value([1,2,4,9,7,10], 3, 20))
    # [1, 2, 4, 20, 9, 7]
"""

def insert_value(arr, index, value):
    """
        Iterate from the end of the list
        to the insertion position/index.
        Keep pushing element to the end.
        Insert the value at insertion index.
    """
    arr_size = len(arr)
    for i in range(arr_size-1, index, -1):
        arr[i] = arr[i-1]
    arr[index] = value
    return arr

print(insert_value([1,2,4,9,7,10], 3, 20))


