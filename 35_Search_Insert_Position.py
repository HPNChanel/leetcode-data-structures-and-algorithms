
from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        target_index = len(nums)
        for i in range(len(nums)):
            if target <= nums[i]:
                target_index = i
                break
        return target_index
