
from typing import List

def majorityElement(nums: List[int]) -> int:
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

"""
Ý tưởng: Sử dụng thuật toán Boyer-Moore Voting, cụ thể:
- Nếu một phần tử là majority (> n/2), thì khi ta ghép cặp với các phần tử khác, nó sẽ vẫn sống sót đến cuối cùng (tức là count sẽ luôn luôn dương (count > 0) nếu kết thúc chương trình)
"""
                

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))
print(majorityElement([3,2,3,2,2]))
print(majorityElement([1,1,1,1,2]))
print(majorityElement([1,1,2,2,2,1,1,1,1,2,1,1,1,1,2]))
