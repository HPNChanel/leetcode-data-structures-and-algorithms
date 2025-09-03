
def convertToTitle(columnNumber: int) -> str:
    n = columnNumber
    rel = []
    
    while n > 0:
        n -= 1
        rel.append(chr(ord('A') + (n % 26)))
        n //= 26
    
    return ''.join(reversed(rel))

print(convertToTitle(1))
print(convertToTitle(28))
print(convertToTitle(701))
"""
Bài toán này phải yêu cầu ta tìm được quy luật tổng quát, ví dụ:
- Từ A-Z: 26 col_nums
- Từ AA-AZ: 26
"""
