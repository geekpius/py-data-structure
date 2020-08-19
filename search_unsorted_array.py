def search_unsorted_array(arr, x):
    #edge case
    arr_size = len(arr)
    if arr_size == 0:
        return 'List is empty'
    
    i = 0

    while i < arr_size:
        if arr[i] == x:
            return str(x)+ ' found'
        i += 1

    return str(x)+' not found'

arr = [5, 1, 3, 4, 2, 6]
x = 2
print(search_unsorted_array(arr,x))