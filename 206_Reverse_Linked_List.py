
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev


"""
Hướng giải:
Bài toán này yêu cầu đảo ngược 1 danh sách liên kết, vì đây là danh sách liên kết đơn, nên buộc ta phải tạo một node phụ để đóng vai trò lưu trữ node hiện tại lúc khi duyệt node tiếp theo, và khi duyệt node tiếp theo, ta hướng point của node tiếp theo về lại node hiện tại
"""
