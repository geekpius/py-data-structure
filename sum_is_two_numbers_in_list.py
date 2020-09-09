
def calculateUnsorted(arr, sum):
    hash_table = set()
    for i in range(len(arr)):
        diff = sum - arr[i]
        if diff in hash_table:
            return "Pair with given sum "+ str(sum) + " is (" + str(arr[i]) + ", " + str(diff) + ")"
        hash_table.add(arr[i])

    return 'Not found'


arr = [1, 4, 45, 6, 10, -8] 
sum = 16
print(calculateUnsorted(arr, sum))



def calculate_sorted_with_pointers(arr, sum):
    start = 0
    end = len(arr)-1
    while start < end:
        if arr[start] + arr[end] > sum:
            end -= 1

        if arr[start] + arr[end] < sum:
            start += 1

        if arr[start] + arr[end] == sum:
            return "Pair with given sum "+ str(sum) + " is (" + str(arr[start]) + ", " + str(arr[end]) + ")" 

    return 'Not found'

arr=[-8, 1, 4, 6, 10, 45]
sum = 16
print(calculate_sorted_with_pointers(arr, sum))

