
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    
    #* If node is leaf
    if not root.left and not root.right:
        return targetSum == root.val
    
    #* Call recursion for left branch and right branch
    return (hasPathSum(root.left, targetSum - root.val)) or (hasPathSum(root.right, targetSum - root.val))


"""
Đặt vấn đề: Có tồn tại một đường đi từ root đến leaf sao cho tổng các giá trị trên đường đi bằng với targetSum?

Hướng giải:
- Có 2 cách chính để giải quyết bài toán này :
    1. Đệ quy:
        + Tại mỗi node, ta trừ đi giá trị node đó khỏi targetSum
        + Nếu đến leaf mà targetSum == node.val, return True
        + Nếu không, tiếp tục đệ quy xuống trái và phải
        + Điều kiện dừng:
            + Node rỗng -> return False
            + Node lá và giá trị còn lại bằng chính node đó -> return True
    2. Sử dụng queue
        + Dùng queue lưu node và tổng hiện tại
        + Với mỗi node:
            + Nếu là leaf và tổng == targetSum -> return True
            + Nếu có con trái/phải -> push vào queue với tổng mới
        + Nếu duyệt hết queue mà không mà không tìm thấy -> return False
"""
