# given a linked list, find if it has a cycle, a cycle occurs when a node in the linked list points back to previous visited node

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next
    

    while slow != fast:
        if not fast or not fast.next:
            return False
        print(slow.val, fast.val)
        slow = slow.next
        fast = fast.next.next

    return True

head = ListNode(1)

head.next = ListNode(2)

head.next.next = ListNode(3)

head.next.next.next = ListNode(4)

head.next.next.next.next = head.next.next
print(has_cycle(head))