
from typing import List 
def maxProfit(prices: List[int]) -> int:
    min_part = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] < min_part:
            min_part = prices[i]
        else:
            if (prices[i] - min_part) > max_profit:
                max_profit = prices[i] - min_part
        
    return max_profit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([5,5,5]))
print(maxProfit([5,4,3,2,10,1]))
print(maxProfit([3,8,2,5,1,7]))
""" Hướng giải quyết:
Với bài toán: Chọn thời điểm mua và tìm thời điểm bán khác trong tương lai sao cho lợi nhuận tối đa hóa cao nhất, tất cả đều nằm trong một danh sách, danh sách bao gồm giá mua và giá bán. Ở đây trả về lợi nhuận cao nhất mà giao dịch đạt được (phải tuần tự)

Ví dụ: prices = [7,1,5,3,6,4]
--> profit: 5. Vì giá mua thấp nhất là 1 (ngày thứ 2) và được bán vào ngày thứ 5 (tức với mức giá cao nhất có thể, trừ mức giá 7), nên lợi nhuận sẽ là 6 - 1 = 5

Ví dụ 2: prices = [7,6,4,3,1]
--> profit: 0. Vì danh sách được sắp xếp theo chiều giảm dần, đồng nghĩa với việc không có sự tăng trưởng về giá dựa trên giá được chọn --> lợi nhuận sẽ là 0

Ý tưởng:
    - Tính toán theo công thức: max(price[j] - price[i]) = max(price[j] - min(price[i]))
    - Tức là, đi từ trái sang phải, ghi nhớ giá thấp nhất đã thấy trước đó (gọi là min_so_far). Ở mỗi ngày j, lợi nhuận tốt nhất nếu bán hôm nay là price[j] - min_so_far. Cập nhật:
        + Nếu price[j] thấp hơn min_so_far --> cập nhật min_so_far
        + Ngược lại, tính lợi nhuận và cập nhật max_profit nếu lớn hơn
    
    Với prices = [7,1,5,3,6,4]
    Bắt đầu với min_so_far = 7, max_profit = 0
    Gặp 1-> thấp hơn -> min_so_far = 1
    Gặp 5 -> lợi nhuận tiềm năng 4 -> max_profit = 4
    Gặp 3 -> lợi nhuận 2 -> max_profit = 4
    Gặp 6 -> lợi nhuận tiềm năng 5 -> max_profit = 5
    Gặp 4 -> lợi nhuận 3-> max_profit = 5
    --> END
"""
