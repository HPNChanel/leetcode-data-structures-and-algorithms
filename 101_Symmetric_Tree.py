
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isMirror(a: TreeNode, b: TreeNode):
    #* If both Null, it symmetric
    if a is None and b is None:
        return True
    #* If one of two is None, it not symmetric
    if a is None or b is None:
        return False
    
    #* Condition to symmetric
    return (a.val == b.val) and isMirror(a.left, b.right) and isMirror(a.right, b.left)

def isSymmetric(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True
    
    return isMirror(root.left, root.right)


"""
Hướng giải:
- Cây đối xứng nghĩa là left subtree là "phần phản chiếu" của right subtree
    + Giá trị gốc con trái = gốc con phải
    + left.left == right.right, left.right == right.left
- Bài toán trên cần viết một hàm phụ isMirror(a, b) để kiểm tra 2 cây có phải là ảnh phản chiếu của nhau hay không
"""
