
from typing import List

def removeElement(nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        return i
    

"""
Hướng giải quyết:
Với bài toán này, ta nên sử dụng two-pointers ổn định thứ tự, tức là kĩ thuật forward overwrite

- Duyệt j từ trái sang phải. Biến i là vị trí kế tiếp cho phần tử hợp lệ
- Nếu nums[j] != val -> gán nums[i] = nums[j], rồi tăng i
- Kết quả: k = i, giữ nguyên relative order của các phần tử còn lại
- Độ phức tạp sẽ là O(n) - duyệt từng phần tử trong nums, độ phức tạp không gian O(1), về số lần ghi thì xấp xỉ số phần tử khác val
Giả sử: nums=[3,2,2,3], val=3
+ j = 0, i = 0 - nums[0]=3 --> bỏ qua
+ j = 1, i = 0 - nums[1]=2 --> nums[0]=2, i+=1
+ j = 2, i = 1 - nums[2]=2 --> nums[1]=2, i+=1
+ j = 3, i = 2 - nums[3]=3 --> bỏ qua
==> k=2, nums[:2] = [2,2]
"""