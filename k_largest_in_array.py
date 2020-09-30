def reverse_merge_sort(arr):
    if len(arr)>1:
        mid = int(len(arr)/2)
        Left = arr[:mid]
        Right = arr[mid:]

        reverse_merge_sort(Left)
        reverse_merge_sort(Right)

        i=j=k=0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Right[j]
                j += 1
            else:
                arr[k] = Left[i]
                i += 1

            k += 1

        while i < len(Left):
            arr[k]=Left[i]
            i+=1
            k+=1

        while j < len(Right):
            arr[k]=Right[j]
            j+=1
            k+=1

        return arr


def find_largest(arr, k):
    result = ''
    i = 0
    while i < k:
        result+= str(arr[i])+', '
        i += 1

    return result


arr = [1, 23, 12, 9, 30, 2, 50]
res = reverse_merge_sort(arr)
print(res)
print(find_largest(res, 3))