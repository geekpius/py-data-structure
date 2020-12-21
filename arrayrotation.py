"""
    Rotate an array by d number
    Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
    Output [3, 4, 5, 6, 7, 1, 2] 
"""


# def left_rotation(arr, d, n):
#     for i in range(d):
#         left_rotate_by_one(arr, n)


# def left_rotate_by_one(arr, n):
#     temp = arr[0]
#     for i in range(n-1):
#         arr[i] = arr[i+1]
#     arr[n-1] = temp




"""
    (A Juggling Algorithm)
    This is an extension of method 2. Instead of moving one by one, divide the array in different sets
"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def left_rotation(arr, d, n): 
    d = d % n 
    g_c_d = gcd(d, n) 
    for i in range(g_c_d): 
          
        # move i-th values of blocks  
        temp = arr[i] 
        j = i 
        while 1: 
            k = j + d 
            if k >= n: 
                k = k - n 
            if k == i: 
                break
            arr[j] = arr[k] 
            j = k 
        arr[j] = temp 




def printArray(arr, size): 
    for i in range(size): 
        print ("% d"% arr[i], end =" ") 

arr = [1, 2, 3, 4, 5, 6, 7] 
left_rotation(arr, 2, 7) 
printArray(arr, 7) 