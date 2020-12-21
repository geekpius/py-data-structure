""" you need to merge and sort these two list """
list1 = [1,2,5,7,8,11]
list2 = [3,4,6,9,10]

def merge_and_sort(list1, list2):
    """ 
    create two pointers for the lists
    sum both list length as merged list length
    an empty list to contain the merged lists
    Note you can use the commented code to achieve the same thing
    """
    list1_pointer = 0
    list2_pointer = 0
    merged_length = len(list1)+len(list2)
    # merged_list = []
    merged_list = [None] * merged_length

    for i in range(merged_length):
        list1_ended =  len(list1) <= list1_pointer
        list2_ended = len(list2) <= list2_pointer
        """ 
            if list1 is not ended and list1 is ended or list1 value is less than list value
            append list1 value onto the empty list
            increment list1 pointer
            else append list2 value onto the empty list
            increment list2 pointer
        """
        if not list1_ended and (list2_ended or list1[list1_pointer] < list2[list2_pointer]):
            # merged_list.append(list1[list1_pointer])
            merged_list[i] = list1[list1_pointer]
            list1_pointer += 1
        else:
            # merged_list.append(list2[list2_pointer])
            merged_list[i] = list2[list2_pointer]
            list2_pointer+= 1
    
    return merged_list
    

print(merge_and_sort(list1, list2))

