import collections

def finder(arr1, arr2):
    d = collections.defaultdict(int)

    for elem in arr2:
        d[elem] += 1
    
    for elem in arr1:
        if elem not in d:
            return elem
        else:
            d[elem] -= 1        


arr1=[2,3,4,5,7]
arr2=[2,3,5,7]

print(finder(arr1, arr2))

# O(nlogn)