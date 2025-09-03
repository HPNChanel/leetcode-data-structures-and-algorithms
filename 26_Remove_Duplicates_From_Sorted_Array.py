
from typing import List

def removeDuplicates(nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1

"""
Hướng giải quyết:
Với bài toán trên, không thể sử dụng Counter để lọc sau đó dùng sorted để sắp xếp được, vì yêu cầu đề bài là thay đổi trực tiếp mảng nums truyền vào (in-place), không được gán lại biến nums (vì khi đó biến cũ không thay đổi; hơn nữa, phải giữ nguyên thứ tự xuất hiện ban đầu của các phần tử

Giải pháp chuẩn: sử dụng 2 con trỏ:
- i trỏ tới vị trí cuối cùng của mảng đã được lọc
- j duyệt qua toàn bộ mảng
- nếu nums[j] != nums[i] thì tăng i và gán nums[i] = nums[j]
"""