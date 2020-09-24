def find_missing(arr):
    for i in range(len(arr)-1):
        if not arr[i]+1 in arr:
            return arr[i]+1



def find_missing1(arr):
    n = len(arr)
    total = ((n+1)*(n+2) // 2)
    
    for i in range(len(arr)):
        total -= arr[i]

    return total


arr = [1, 2, 4, 6, 3, 7, 8]
print(find_missing(arr))
print(find_missing1(arr))