
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root: Optional[TreeNode]) -> bool:
    def check(node: TreeNode) -> Optional[TreeNode]:
        if node is None:
            return 0

        left = check(node.left)
        if left == -1: return -1
        
        right = check(node.right)
        if right == -1: return -1
        
        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)
    
    return check(root) != -1
    

"""
Hướng giải:
- Một cây được gọi là height-balanced nếu:
    + Với mọi node, chênh lệch chiều cao giữa cây con trái và phải <= 1
    + Đồng thời, cả hai cây con cũng phải balance
Nói cách khác: balance không chỉ check ở root, mà phải lan xuống toàn bộ cây

- Ở đây, ta viết một giải thuật đệ quy trả về chiều cao của một cây con, nhưng với điều kiện:
+ Nếu subtree không cân bằng, ta trả về giá trị đặc biệt (ví dụ -1) để báo hiệu fail, không cần phải tính tiếp
+ Nhờ vậy, mỗi node chỉ được duyệt 1 lần

Ở đây ta lưu ý ở điểm: lần gọi đầu tiên vẫn kiểm tra left, right == -1, vì:
- Luồng đệ quy là post order
    + Gọi check(root) -> chưa rõ gì
    + check sẽ đi xuống đáy liên tục (đi đến None) -> trả về 0 --> tức chiều cao cây rỗng
    + tiến hành quay lên dần (quá trình call stack), tại mỗi node ta lần lượt nhận được kết quả từ trái, rồi phải:
        + Nếu một bên đã là -1, ta ngưng và trả -1 luôn
        + Nếu cả 2 bên là chiều cao, ta kiểm tra độ lệch, nếu lệch > 1, tạo -1 tại node này
    + -1 (nếu xuất hiện) lan ngược lên đến gốc

Nói cách khác thì, ta không cần biết trước -1 ở lần gọi đầu, ta chỉ cần tin vào: khi node con trả về, giá trị ấy hoặc là height, hoặc là -1 (vì vậy, kiểm tra == -1) luôn hợp lệ
"""
