def merge_sort(arr):
    if len(arr)>1:
        mid = int(len(arr)/2)
        Left = arr[:mid]
        Right = arr[mid:]

        merge_sort(Left)
        merge_sort(Right)

        i=j=k=0
        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1

            k += 1

        while i < len(Left):
            arr[k]=Left[i]
            i+=1
            k+=1

        while j < len(Right):
            arr[k]=Right[j]
            j+=1
            k+=1

        return f"{arr}\n----------------\nTwo smallest elements ({arr[0]}, {arr[1]})"



import sys
def find_first_second(arr):
    first = second = sys.maxsize
    for i in arr:
        if i < first:
            second, first = first, i
        elif i< second and i != first:
            second = i

    if first != second:
        return f"Two smallest elements ({first}, {second})"
    else:
        return f"only first number {first}"



arr = [12, 25, 8, 55, 10, 33, 17, 11]

# print(merge_sort(arr))
print(find_first_second(arr))
