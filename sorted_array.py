def binarySearch(arr, start, end, key):
    """
        if end index is greater than start index meaning there's more elements
        if end index is equal to start index meaning there's one elements
        else we return -1
    """
    if end >= start:
        # divide start index + end index by 2 to get element in the middle of the list
        mid = int((start+end)/2)
        
        # if the key is equal to the element in the middle of the list return middle index
        if key == arr[mid]:
            return mid
        
        """
            if the key is greater than the element in the middle of the list do recursion 
            start searching from the next element to the middle to the end

            if the key is less than the element in the middle of the list do recursion 
            start searching from the start to previous element to the middle
        """
        
        if key > arr[mid]:
            return binarySearch(arr, (mid+1), end, key)
        else:
            return binarySearch(arr, start, (mid-1), key)

    return -1

    # O(logn)


# arr = [5, 6, 7, 8, 9, 10, 11] 
# n = len(arr)-1 
# key = 5

# print(binarySearch(arr, 0, n, key))


def sortedInsertion(arr, n, cap, key):
    """
        we increase our list to take up more elements and let it be our capacity.
        if initial size of the list is greater or equal to capacity means we can't do insertion, 
        list is up to end and we return the initial size
    """
    if n >= cap:
        return n
    

    # initial list size since we are starting from zero will be n-1
    i = n-1
    # whiles size is less than zero and value of the current element is greater than key, keep looping
    while i >= 0 and arr[i] > key:
        # start pushing the current element to the next
        arr[i+1] = arr[i]
        i -= 1
    arr[i+1]=key # if current element is not greater than key, insert key to next element

    
    """
        The new size will be initial size + 1 (n+1)
    """
    new_arr = [None] * (n+1)
    for i in range(n+1):
        new_arr[i] = arr[i]

    return new_arr

# arr = [5, 6, 8, 9, 10, 11] 
# arr.append(0)
# n = 6
# cap = len(arr)
# key = 7

# print(sortedInsertion(arr, n, cap, key))


def deleteElement(arr, n, key):
    # use binary search to find the index of the key
    pos = binarySearch(arr, 0, n-1, key)

    if pos == -1:
        return 'Key not found'

    # loop from the index of the found key to the end -1(for not getting out of range)
    for i in range(pos, n-1):
        arr[i]= arr[i+1]
    
    
    """
        The new size will be initial size -1 (n-1)
    """
    new_arr = [None] * (n-1)
    for i in range(n-1):
        new_arr[i] = arr[i]

    return new_arr




arr = [5, 6, 7, 8, 9, 10, 11] 
n = len(arr)
key = 6

# x = filter(lambda a: a!= key, arr)
# print(list(x))

print(deleteElement(arr, n, key))