
"""
* Phân tích bài toán
- Nếu danh sách giao nhau tại một node, từ node đó trở đi, cả 2 danh sách sẽ giống nhau
Ý tưởng:
- Dùng kỹ thuật 2 con trỏ p1 và p2
    + Duyệt danh sách, nếu một con trỏ đến cuối thì chuyển sang danh sách kia
    + Nếu có điểm giao nhau, cả hai sẽ gặp nhau ở node giao nhau
    + Nếu không có điểm giao nhau, cả hai sẽ gặp nhau tại NULL
"""

class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

from typing import Optional

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None
    
    p1, p2 = headA, headB
    
    while p1 != p2:
        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA
    
    return p1
