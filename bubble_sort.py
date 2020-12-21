
"""
    Checking to break the inner loop if there was no swap is a way
    to optimized our bubble sort
"""
def bubble_sort(A):
    for i in range(len(A)):
        swapped = False

        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                swapped = True
        
        if not swapped:
            break

    return A

A = [64, 25, 12, 22, 11] 
print(bubble_sort(A))

# time complexity O(n square)
# space complexity O(1)