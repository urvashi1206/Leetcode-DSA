# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def deleteMiddle(head: ListNode) -> ListNode:
        if(head.next is None):
            return None
        fast=head
        slow=head
        while(fast.next.next is not None and fast.next.next.next is not None):
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head

def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Example usage:
arr = [1, 2, 5, 6, 3 ,7]
head = build_linked_list(arr)
delete_middle_head = deleteMiddle(head)
print_linked_list(delete_middle_head)