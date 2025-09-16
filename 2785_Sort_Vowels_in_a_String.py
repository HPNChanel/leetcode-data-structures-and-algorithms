
def sortVowels(s: str) -> str:
    vowels = set("AEIOUaeiou")
    idx = [i for i, ch in enumerate(s) if ch in vowels]
    vals = sorted((s[i] for i in idx), key=lambda c: ord(c))
    s_list = list(s)
    for i, ch in zip(idx, vals):
        s_list[i] = ch
    
    return "".join(s_list)


"""
Hướng giải:
- Thuật toán trên lấy ý tưởng là dựa vào index đã có trên s cho mỗi nguyên âm, ta cần lọc ra nguyên âm và chỉ mục của nguyên âm đó trong chuỗi s thành một list các tuple, sau đó sort danh sách trên theo nguyên tắc: mã ascii tăng dần, lưu vào biến vals (là 1 danh sách)
- Bước tiếp theo là biến chuỗi s thành 1 danh sách, sau đó, biến đổi chuỗi s dựa theo thứ tự đã sắp xếp trong vals, bằng cách gán các ký tự tương ứng trong vals để thay thế các ký tự tương ứng trong s
"""
