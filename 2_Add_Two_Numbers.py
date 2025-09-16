
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    carry = 0
    
    while l1 or l2  or carry:
        x = l1.val if l1 else 0        
        y = l2.val if l2 else 0
        
        s = x + y + carry
        
        carry = s // 10
        
        cur.next = ListNode(s % 10)
        cur = cur.next
        
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
    return dummy.next

        

"""
Hướng giải:
- Duyệt đồng thời l1 và l2
- Mỗi bước lấy x = l1.val (hoặc 0 nếu hết), y = l2.val (hoặc 0)
- Tính sum = x + y + carry | Lấy digit = sum % 10, cập nhật carry = sum // 10 (cách này để handle phần có nhớ sau khi vượt quá 9)
- Gắn digit vào đuôi kết quả
- Tiếp tục cho đến khi cả hai list hết và carry = 0 
<-> Dùng dummy head để dễ nối node
Time Complexity: O(max(m, n))
Space Complexity: O(1)

Nói một cách dễ hiểu, thì ta không cần quan tâm danh sách đó theo thứ tự đảo ngược, chỉ theo quy luật, nếu cộng mà vượt quá 9, số đó sẽ thành 0 và nhớ 1, 1 này sẽ được cộng vào số tiếp theo
"""
