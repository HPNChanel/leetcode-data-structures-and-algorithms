
def isIsomorphic(s: str, t: str) -> bool:
    
    s2t = {}
    t2s = {}
    
    for i, j in zip(s, t):
        if i in s2t:
            if s2t[i] != j:
                return False
        else:
            s2t[i] = j
        
        if j in t2s:
            if t2s[j] != i:
                return False
        else:
            t2s[j] = i
    return True
    


"""
Ý tưởng:
- Bài toán này đề cập đến sự đồng dạng, ví dụ, 2 chuỗi đồng dạng như sau:
s: add
t: pee
Các ký tự trong chuỗi s có thể được THAY THẾ ÁNH XẠ tương ứng để tạo thành chuỗi t, và ngược lại
a mapping to p, d mapping to e
Giải thích: Tất cả lần xuất hiện trong 1 ký tự đều phải được thay thế bằng 1 ký tự khác trong khi vẫn giữ nguyên thứ tự của các ký tự. Không có 2 ký tự nào có thể ánh xạ vào cùng 1 ký tự, nhưng 1 ký tự có thể ánh xạ chính nó

Tuy nhiên, 2 chuỗi sau là không đồng dạng:
s: add
t: bar
a mapping to b, d mapping to a, but d cannot still mapping to r

Hướng giải quyết:
- Tạo 2 map để kiểm tra cả 2 chiều:
    + s2t[i] = j nếu chưa có thì gán, nếu đã có thì phải bằng j
    + t2s[j] = i tương tự, nếu j đã gán cho ký tự khác -> False ngay lập tức
"""
