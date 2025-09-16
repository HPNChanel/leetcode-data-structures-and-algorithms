
from collections import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []
    
    def inorder(node: TreeNode):
        if not node:
            return
        
        inorder(node.left)  #* First, traverse the left part
        res.append(node.val)  #* If None in one branch, add the parent node to res, continue traverse to right branch
        inorder(node.right)  #* Traverse until None all
    
    inorder(root)
    return res


"""
    Ở bài toán này, ta duyệt theo hướng Inorder, tức là đi vào cây con bên trái trước, sau đó lấy giá trị của node hiện tại, rồi mới sang cây con bên phải.
    Cách tối ưu nhất, sử dụng đệ quy
    
    Ví dụ: root = [1, null, 2, 3]
    Cây này sẽ được dựng như sau:
       1
        \
         2
        /
       3

    Thuật toán trên sẽ được triển khai như sau:
    - Bắt đầu duyệt từ node bên trái của node 1 --> null --> res.append(1)
    - Bắt đầu duyệt node bên phải của 1, có 2
    - Duyệt xuống node trái của node 2 --> node 3
    - Duyệt xuống node trái của node 3 --> null --> res.append(3)
    - Duyệt xuống bên phải node 3 --> null --> res.append(2)
    
    ==> res = [1,3,2]
"""
