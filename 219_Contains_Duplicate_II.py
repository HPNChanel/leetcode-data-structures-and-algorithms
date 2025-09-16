
from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    dict_nums = {}
    
    for i in range(len(nums)):
        if nums[i] in dict_nums:
            if abs(i - dict_nums[nums[i]]) <= k:
                return True
            else:
                dict_nums[nums[i]] = i
        else:
            dict_nums[nums[i]] = i
    
    return False


print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,0,1,1], 1))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))

"""
Bài toán này yêu cầu nếu có 2 chỉ số phân biệt i và j trong mảng mà thỏa mãn nums[i] == nums[j] và abs(i - j) <= k

Ý tưởng: vòng lặp lồng nhau sẽ không hiệu quả, vì có trường hợp chắc chắn sẽ duyệt hết một lần mảng sau đó mới chuyển sang phần tử kế tiếp.
Ở đây, ta sẽ cho phần tử vào một hash table, với giá trị khóa (key) sẽ là element của mảng, giá trị tương ứng sẽ là chỉ mục xuất hiện gần nhất của phần tử đó

PSEUDO CODE

"""


