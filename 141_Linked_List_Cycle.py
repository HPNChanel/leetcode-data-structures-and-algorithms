
from typing import Optional

class ListNode:
    def __init__(self, val ):
        self.val = val
        self.next = None
        
        
def hasCycle(head: Optional[ListNode]) -> bool:
    slow = fast = head   #* Xuất phát từ đầu danh sách liên kết
    while fast and fast.next:  #* Mỗi vòng lặp luôn kiểm tra fast và fast.next khác None trước khi fast = fast.next.next
        slow = slow.next  #* Slow đi 1 bước
        fast = fast.next.next   #* Fast đi 2 bước
        if slow is fast:  #* Xét trường hợp hai con trỏ slow và fast gặp nhau
            return True   #* Tức là danh sách liên kết có cycle
    return False  #* Ngược lại, danh sách liên kết không có cycle
    


"""
Hướng giải:

Với bài toán trên, cách tối ưu nhất là sử dụng thuật toán Floyd's Tortoise & Hare (thuật toán rùa và thỏ - ở đây là đại diện cho 2 con trỏ nhanh và chậm). Cụ thể:
    + Khai báo một con trỏ slow, con trỏ này bước đi tối đa là 1, khai báo thêm con trỏ fast, con trỏ này bước đi tối đa là 2. Nếu tồn tại cycle, chúng chắc chắn sẽ "gặp" nhau bên trong vòng

***Chứng minh***
- Giả sử danh sách gồm phần thẳng dài `a` node rồi vào vòng có độ dài `b`:
    + Sau `a` bước, slow vào vòng. Lúc này khoảng cách giữa fast và slow trong vòng tăng 1 mỗi bước lặp (vì fast đi 2, slow đi 1)
    + Trong không quá `b` bước, khoảng cách mod `b` sẽ về 0 --> gặp nhau. Độ phức tạp là O(a + b) <= O(n)
"""
