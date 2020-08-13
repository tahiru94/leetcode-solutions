class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def swap_pairs(head):
    if head:
        if head.next:
            head.val, head.next.val = head.next.val, head.val
            if head.next.next:
                swap_pairs(head.next.next)
    return head