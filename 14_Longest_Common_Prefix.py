
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

"""
Đoạn code trên có thể được phân tích như sau:
- Nếu mảng rỗng, trả về ""

- Ta tạo một biến prefix, biến này sẽ lưu trữ phần tử đầu tiên của mảng để làm prefix
- Duyệt mảng (trừ từ đầu tiên được lấy ra làm mốc)
- Tạo một vòng lặp while, có tác dụng là kiếm tra nếu prefix có khớp với các từ hoặc phần đầu tiên của các từ hay không, nếu không, tiến hành loại bỏ phần tử cuối của prefix để sao cho lấy được mẫu khớp với các từ (hoặc phần đầu của các từ) còn lại. Nếu prefix rỗng, tức không có từ nào khớp, trả về ""
"""
print(longestCommonPrefix(["flower","flow","flight"]))  # fl
print(longestCommonPrefix(["dog","racecar","car"]))     # ""
