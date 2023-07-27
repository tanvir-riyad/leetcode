class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    if not head or not head.next:
        return False
    
    current = head
    prev = None

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


head = ListNode('a')
head.next = ListNode('b')
head.next.next = ListNode('c')
head.next.next.next = ListNode('d')

reverse_head = reverse_linked_list(head)

print(reverse_head.next.val)