from collections import Counter
from typing import List
def singleNumber(self, nums: List[int]) -> int:
        
        dict_nums = Counter(nums)
        rel = 0

        for i in dict_nums.keys():
            if dict_nums[i] == 1:
                rel = i
                break
        
        return rel