def ceil_and_floor(arr, key):
    low = 0
    high = len(arr)-1

    if arr[low] > key:
        return f"No floor, ceil={arr[low]}"
    elif arr[low] == key:
        return f"floor={arr[low]}, ceil={arr[low]}"

    if arr[high] < key:
        return f"floor={arr[high]}, No ceil"
    elif arr[high] == key:
        return f"floor={arr[high]}, ceil={arr[high]}"

    for i in range(1, len(arr)-1):
        if arr[i] > key:
            return f"floor={arr[i-1]}, ceil={arr[i]}"
        if arr[i] == key:
            return f"floor={arr[i-1]}, ceil={arr[i+1]}"
        

def binary_ceil_and_floor(arr, low, high, key):
    if key <= arr[low]:
        return low

    if key > arr[high]:
        return -1

    mid = int((low+high)/2)
    if arr[mid] == key:
        return mid

    if arr[mid] < key:
        if mid+1 <= high and key <= arr[mid+1]:
            return mid+1
        else:
            binary_ceil_and_floor(arr, mid+1, high, key)
    else:
        if mid-1 >= low and key <= arr[mid-1]:
            return mid+1
        else:
            binary_ceil_and_floor(arr, low, mid-1, key)


arr= [1, 2, 8, 10, 10, 12, 19]
key = 19

index = binary_ceil_and_floor(arr, 0, len(arr)-1, key)
print(f"ceil={arr[index]}") if index != -1 else print('none')