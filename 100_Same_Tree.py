
from collections import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #* Case 1: Both p and q are None
    if not p and not q:
        return True
    
    #* Case 2: One of two node is None
    if not p or not q:
        return False
    
    #* Case 3: Same structure but differences at value
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

"""
Ý tưởng:
- Đây là dạng so sánh đệ quy
    + Nếu cả 2 node đều rỗng (None) -> giống nhau
    + Nếu một node rỗng, node kia không rỗng -> khác nhau
    + Nếu cả hai có giá trị khác nhau -> khác nhau
    + Ngược lại, ta tiếp tục so sánh cây con trái và cây con phải
"""
