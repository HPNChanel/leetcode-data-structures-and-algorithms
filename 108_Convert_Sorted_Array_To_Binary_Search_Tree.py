
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    
    def build(l: int, r: int) -> Optional[TreeNode]:
        if l > r:
            return None
        mid = (l + r) // 2  #* or (l + r + 1) // 2
        root = TreeNode(nums[mid])  #* Set the root equal to the middle part of array
        root.left = build(l, mid - 1)  #* Check all nodes from left branch
        root.right = build(mid + 1, r)  #* Check all nodes from right branch
        return root

    return build(0, len(nums) - 1)


""" 
Ý tưởng:
- Muốn cho cây có cấu trúc height balance, ta phải chọn điểm cân bằng nằm giữa mảng làm root, ví dụ
    + root = (l + r) // 2
    + root = (l + r + 1) // 2
- Bên trái mảng -> cây con trái; bên phải mảng -> cây con phải
- Lặp lại đệ quy. Mỗi bước thu nhỏ bài toán một nửa
- Độ phức tạp: O(n) cho time, O(log n) cho space vì phân bổ bộ nhớ
"""
