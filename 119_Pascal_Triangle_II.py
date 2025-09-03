
from typing import List

def getRow(rowIndex: int) -> List[int]:
    triangle = []
    row = [1]
    
    for _ in range(rowIndex):
        triangle.append(row[:])
        row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
    
    return row

print(getRow(3))
print(getRow(0))
print(getRow(1))
