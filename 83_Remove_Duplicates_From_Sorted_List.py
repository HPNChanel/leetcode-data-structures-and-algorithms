
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

"""
Hướng giải:
Với bài toán loại bỏ node trùng lặp trong danh sách liên kết và kết quả trả về là một danh sách với các node riêng biệt theo thứ tự tăng dần
Ý tưởng:
- Vì list đã sorted, nên nếu có duplicates thì chúng sẽ nằm cạnh nhau
- Ta chỉ đơn giản là duyệt từ đầu đến cuối, so sánh current.val với current.next.val:
    + Nếu giống nhau, bỏ qua current.next (cho current.next = current.next.next)
    + Nếu khác, di chuyển current = current.next
"""
