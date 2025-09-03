
from typing import Optional

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def mergeTwoLists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        temp = Node(-1)
        current = temp

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2

        return temp.next


"""Bài toán trên có thể được giải thích như sau
- Ta có một class Node được xây dựng sẵn, Node này đại diện cho các node cho 2 danh sách liên kết trên

- Ta khởi tạo một temp node, node này có mục đích là node đại diện tạm thời cho các node chạy trong danh sách liên kết, khởi tạo ở giá trị -1
- Khởi tạo thêm một node current để đại diện cho đuôi của danh sách kết quả
- Duyệt đồng thời cả 2 danh sách (điều kiện là cả 2 danh sách phải chứa node):
    + Nếu giá trị của node trong list1 nhỏ hơn giá trị của node trong list2 -> để current trỏ tới list1, node hiện tại trong list1 sẽ trỏ đến node tiếp theo trong list1
    + Ngược lại, current sẽ trỏ tới list2, node hiện tại trong list2 sẽ trỏ đến node tiếp theo trong list2
    + Sau mỗi lần kiểm tra điều kiện, để current trỏ đến node tiếp theo để tiến hành duyệt

- Nếu list1 vẫn còn phần tử, gán current cho list1
- Bỏ đi node giả hiện tại, trỏ đến trạng thái tiếp theo
"""
