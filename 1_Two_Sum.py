
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
def twoSum(nums: list[int], target: int) -> list[int]:
    len_nums = len(nums)
    rel = []
    i = 0
    j = i + 1
    
    while i < j:
        if nums[i] + nums[j] == target:
            rel.extend(i, j)
            break
        elif j == len_nums - 1:
            i += 1
            j = i + 1
        else:
            j += 1
    
    return rel
    