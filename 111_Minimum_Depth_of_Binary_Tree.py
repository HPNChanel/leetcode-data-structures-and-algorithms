
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def minDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    q = deque([(root, 1)])
    while q:
        node, depth = q.popleft()
        if not node.left and not node.right:  #* Meet the first node
            return depth
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
    
    """
    Ở đây, nó sẽ duyệt liên tục cho đến khi nó tìm được một node không có node trái và không có node phải
    """


"""
Đặt vấn đề: Chiều sâu nhỏ nhất của một cây là số lượng node trên đường ngắn nhất từ root đến leaf node gần nhất, leaf node = node không có node con trái và phải.

Hướng giải: Breadth First Search - sử dụng hàng đợi
- Ta dùng BFS duyệt từ trên xuống, khi gặp node nào mà không có node con trái và phải -> return ngay depth
"""
