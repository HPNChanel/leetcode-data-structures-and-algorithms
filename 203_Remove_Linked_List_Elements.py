
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next


""" 
Ý tưởng:
- Dummy node giúp tránh các case đặc biệt khi head chính là node cần xóa
- Duyệt list, nhưng luôn kiểm tra current.next
- Nếu thấy giá trị trùng, bỏ qua bằng cách nối sang current.next.next
- Nếu không, chỉ đơn giản là trỏ sang node tiếp theo
- Trả về dummy.next (tức là new head hiện tại)
"""
    