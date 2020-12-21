def find_element(arr, low, high, key):

    """" O(n) """
    # for i in range(len(arr)):
    #     if key == arr[i]:
    #         return i
    # return -1


    """" O(n) """
    # while low <= high:
    #     if arr[low] == key:
    #         return low
        
    #     if arr[high] == key:
    #         return high

    #     low += 1
    #     high -= 1

    # return -1


    """" O(LOG n) """
    if low <= high:
        mid = (low+high) // 2
        
        if arr[mid] == key:
            return mid

        if arr[low] <= arr[mid]:
            if key >= arr[low] and key <= arr[mid]:
                return find_element(arr, low, mid-1, key)
            return find_element(arr, mid+1, high, key)


        if key >= arr[mid] and key <= arr[high]:
            return find_element(arr, mid+1, high, key)
        return find_element(arr, low, mid-1, key)


    return -1




arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 10
low =0 
high = len(arr)-1
print(find_element(arr, low, high, key))