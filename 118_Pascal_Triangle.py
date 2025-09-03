
from typing import List

def generate(numRows: int) -> List[List[int]]:
    triangle = []
    row = [1]
    
    for _ in range(numRows):
        triangle.append(row[:])  #* Copy toàn bộ hàng hiện tại
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]  #* Tổng của 2 phần tử liên tiếp nhau trong cùng 1 hàng
    
    return triangle


print(generate(5))
"""
Giải thích:
    - Tam giác Pascal là một cấu trúc số học, trong đó, mỗi số là tổng của 2 số phía trên nó (trái và phải). Nó bắt đầu từ đỉnh là 1 và mở rộng dần xuống dưới
    Hàng 0:         1
    Hàng 1:       1   1
    Hàng 2:     1   2   1
    Hàng 3:   1   3   3   1
    Hàng 4: 1   4   6   4   1
Công thức:
    - Phần tử ở hàng n, cột k (đánh từ 0) chính là tổ hợp C(n, k)
    - Ví dụ ở hàng 4, cột 2 --> C(4, 2) = 6
Hướng tiếp cận: thường thì có 2 hướng chính
    - DP (quy hoạch động)
        + Bắt đầu từ hàng 0 = [1]
        + Mỗi hàng mới = [1] + (từng tổng của 2 số liên tiếp ở trong hàng trước) + [1]
        Ví dụ:
        Hàng 1: [1,1]
        Hàng 2: [1] + [1+1] + [1] = [1, 2, 1]
    - Dùng công thức tổ hợp (không khuyến nghị)
Độ phức tạp: O(n^2)
"""
