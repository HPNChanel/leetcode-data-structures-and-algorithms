
from typing import List

def plusOne(self, digits: List[int]) -> List[int]:
    rel = int(''.join(str(i) for i in digits)) + 1
    rel = [int(i) for i in str(rel)]
    return rel