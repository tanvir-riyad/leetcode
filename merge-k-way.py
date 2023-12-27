class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    if not lists:
        return None
    
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged =merge_two_lists(l1, l2)
            print(to_list(merged))
            merged_lists.append(merged)
        
        
        lists = merged_lists
    
    return lists[0]

def merge_two_lists(l1, l2):
    dummy = ListNode()
    current = dummy
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    if l1:
        current.next = l1
    elif l2:
        current.next = l2
    
    return dummy.next

def from_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage:
lists = [[1,4,5], [1,3,4,6,9], [2,6]]
list_nodes = [from_list(lst) for lst in lists]
result = merge_k_lists(list_nodes)
print(to_list(result))
