def merge_list(arr1, arr2):
    i=j=0
    arr3 = []
    while i <len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    while i < len(arr1):
        arr3.append(arr1[i])
        i+=1

    while j < len(arr2):
        arr3.append(arr2[j])
        j+=1

    return arr3


def find_median(arr):
    n = len(arr)
    if n%2 == 0:
        mid = int(n/2)
        av_mid = (arr[mid-1]+arr[mid])/2
        return int(av_mid)
    else:
        mid = int((n-1)/2)
        return arr[mid]


arr1 = [1, 12, 15, 26, 38] 
arr2 = [2, 13, 17, 30, 45] 
arr3 = merge_list(arr1, arr2)
print(arr3)
print('---------------------------\n')
print(find_median(arr3))