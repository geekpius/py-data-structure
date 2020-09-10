
def bubble_sort(A):
    for i in range(len(A)):
        
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]

    return A

A = [64, 25, 12, 22, 11] 
print(bubble_sort(A))

# time complexity O(n square)
# space complexity O(1)