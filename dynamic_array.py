import ctypes
import sys



"""
    Creating dynamic array from scratch
"""
class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity) # this will call make array to build it
    
    def __len__(self):
        return self.n # return the size of the array

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!') # this triggers when the array is out of bound

        return self.A[k] # return the reference in the array

    def append(self, ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x if capacity isn't enough

        self.A[self.n] = ele # replace the element to the last reference
        self.n += 1

    def _resize(self, new_cap):
        B = self.make_array(new_cap) #make a new array call B
        for k in range(self.n):
            B[k] = self.A[k] #referencing from array A into B

        self.A = B
        self.capacity = new_cap # reseting capacity to the new capacity

    def make_array(self, new_cap):
        return (new_cap*ctypes.py_object)() # using a library call ctypes to make the array



# arr = DynamicArray()
# n = 10
# for i in range(n):
#     l = len(arr)
#     s = sys.getsizeof(arr)
    
#     print("Array Length: {0}  ---- Array Size in bytes: {1}".format(l, s))
#     arr.append(n)