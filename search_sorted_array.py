def search_sorted_array(arr, start, end, value):
    """
        Iterative
    """
    # while start <= end:
    #     midpoint = int((start+end)/2)
    #     if arr[midpoint] ==  value:
    #         return str(value)+ ' found'

    #     if arr[midpoint] < value:
    #         start = midpoint + 1
    #     else:
    #         end = midpoint - 1

    # return str(value)+ ' not found'

    """
        Recursive
    """

    if end >= start:
        midpoint = int((start+end)/2)
        if arr[midpoint] == value:
            return str(value)+ ' found'
        
        if arr[midpoint] < value:
            search_sorted_array(arr, start, midpoint-1, value)
        else:
            search_sorted_array(arr, midpoint+1, end, value)

    return str(value)+ ' not found'




arr = [1, 2, 3, 4, 5, 6]
start = 0
end = len(arr)-1
x = 1
print(search_sorted_array(arr, start, end ,x))