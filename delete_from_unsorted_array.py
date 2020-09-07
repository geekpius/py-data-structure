def findElement(arr, n, key): 
    for i in range(n):
        if arr[i] == key:
            return i

    return -1



def delete(arr, n, key):
    pos = findElement(arr, n, key)
    if pos == -1:
        return 'Element not found in the list'
    
    for i in range(pos, n-1):
        arr[i] = arr[i+1]
    
    new_arr = [None]*(n-1)
    
    for i in range(n-1):
        new_arr[i]=arr[i]

    return new_arr




arr = [12, 34, 10, 6, 40] 
key = 50
n = len(arr) 

print(arr)
print(delete(arr, n, key))