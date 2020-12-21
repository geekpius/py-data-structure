def merge_sort(arr):
    if len(arr) > 1:
        #find the middle index
        mid = len(arr) // 2
        
        # Split your arr into two Left and Right
        Left = arr[:mid]
        Right = arr[mid:] 

        #sorting
        merge_sort(Left)
        merge_sort(Right)

        #merging
        i = j = k = 0
        while i < len(Left)  and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1

            k += 1


        #checking for left and right
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1

        return arr

    return arr



# O(logN)
# O(n)
# only sorting out place and its really good for linked list
arr = [12, 11, 13, 5, 6, 7]
print(merge_sort(arr))