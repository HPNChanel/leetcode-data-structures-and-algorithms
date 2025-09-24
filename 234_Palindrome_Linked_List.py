
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: Optional[ListNode]) -> bool:
    rel = []
    
    current = head
    
    while current:
        rel.append(current.val)
        current = current.next
    return rel == rel[::-1]

def build_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

print(isPalindrome(build_linked_list([1,2,2,1])))
print(isPalindrome(build_linked_list([1,2])))
print(isPalindrome(build_linked_list([1])))
