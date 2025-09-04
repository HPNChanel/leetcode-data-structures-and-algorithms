
def titleToNumber(columnTitle: str) -> int:
    rel = 0
    for char in columnTitle:
        rel = rel * 26 + (ord(char) - ord('A') + 1)
    
    return rel
    

char = input()

print(titleToNumber(char))

"""
Công thức: Value = ord(char) - ord('A') + 1
    Ví dụ: A = ord(A) - ord('A') + 1 = 65 - 65 + 1 = 1
    Tổng giá trị quy đổi: 
    result = result * 26 + (ord(char) - ord('A') + 1)
"""
