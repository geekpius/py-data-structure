"""
    input [1,2,-1,3,4,10,10,-10,-1]
    output 29
"""

def cont_sum(arr):
    if len(arr) == 0:
        return 'List is empty'

    sum = 0
    i = 1
    # for i in range(len(arr)):
    #     if i > 0 and arr[i] >= 0:
    #         sum += arr[i]
    while i < len(arr):
        if arr[i] >= 0:
            sum += arr[i]
        i += 1

    return sum


print(cont_sum([1,2,-1,3,4,10,10,-10,-1]))