
from typing import List


def summaryRanges(nums: List[int]) -> List[str]:
    rel = []
    if not nums:
        return rel
    
    a = 0
    for b in range(1, len(nums) + 1):
        if b == len(nums) or nums[b] != nums[b - 1] + 1:
            if a == b - 1:
                rel.append(f"{nums[a]}")
            else:
                rel.append(f"{nums[a]}->{nums[b - 1]}")
            a = b
    
    return rel


print(summaryRanges([0,1,2,4,5,7]))
print(summaryRanges([0,2,3,4,6,8,9]))
    


"""
Đặt vấn đề: Bài toán cho trước một mảng số nguyên được sắp xếp tăng dần, các phần tử không trùng nhau. Một đoạn [a, b] là tập hợp các số nguyên từ a đến b (tập bao gồm cả a và b). Trả về danh sách các đoạn NHỎ NHẤT ĐÃ SẮP XẾP bao gồm chính xác tất cả các số trong mảng
Lưu ý, mỗi phần tử trong nums phải bao bọc bởi chính xác 1 phần tử trong đoạn, và không có số nguyên x nào nằm trong đoạn mà không nằm trong nums

Ví dụ: "a->b" nếu a != b | "a" nếu a == b

Ý tưởng: Ta khởi tạo một mảng con trong lúc lặp, hai phần tử là a và b là biến vòng lặp, thêm phần tử a vào mảng con trước, nếu b - a = 1 --> thêm b vào mảng, sau đó gán b cho a hiện tại và tiếp tục duyệt b cho đến khi b - a > 1, append 2 phần tử đầu và cuối của mảng con đó theo format result, sau đó, xóa mảng

PSEUDO CODE

rel = []

for a in range(len(nums))
    sub = []
    for b in range(1, len(nums))
        if nums[b] - nums[a] equals to 1
            sub.extend(a, b)
        else
            rel.append(f"{sub[0]->sub[-1]}")
            rel.append(f"{b}")
            sub = []
        a = b

"""
