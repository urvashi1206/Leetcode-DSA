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

def oddEvenList(head: ListNode) -> ListNode:
        t1=head
        if head is None:
            return
        if head.next is None:
            return head
        t2=head.next
        temp=head.next
        while t1 and t2 and t1.next.next:
            t1.next=t1.next.next
            t1=t2.next
            t2.next=t1.next
            t2=t1.next
        t1.next=temp

        return head

def print_linked_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Example usage:
arr = [1, 2, 3, 4, 5]
head = build_linked_list(arr)
oddeven_head = oddEvenList(head)
print_linked_list(oddeven_head)