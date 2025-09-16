
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def maxDepth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return 1 + max(left_depth, right_depth)

"""
Hướng giải:
- Độ sâu của cây tại một node = 1 + max(độ sâu cây con trái, độ sâu cây con phải). Node rỗng có độ sâu 0. Đây là một quy nạp tự nhiên -> sử dụng DFS đệ quy. Mỗi lần gọi sẽ tính toán số lượng left_depth và right_depth, mỗi đơn vị sẽ tượng trưng cho số lượng node ở mỗi bên
"""
