""" a function to reverse a list """
def reserve(head_of_list):
    current_node = head_of_list
    next_node = None
    prev_node = None

    """ current node will hold the input, we don't know the next and prev nodes of the current node """

    """ while we still have current node we iterate and reserve the list """
    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = current_node.next
    return prev_node