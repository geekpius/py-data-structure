"""
    Given an integer array, output all the unique pairs that sum up to a specific value k
"""

def pair_sum(arr, k):
    if len(arr)< 2:
        return 'No set found'
    
    seen = set()
    output = set()
    for elem in arr:
        # find the target elem
        target = k - elem
        if target not in seen:
            seen.add(elem)
        else:
            min_max_tuple = (min(elem, target), max(elem, target))
            output.add(min_max_tuple)
    final = list(output)
    if final is None:
        return 'No set found'
    return '\n'.join(map(str, final))

print(pair_sum([3,3,2,1,5,1,4], 6))

# O(n)