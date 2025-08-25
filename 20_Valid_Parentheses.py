
class Stack:
    def __init__(self):
        self.data = []
    def push(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop() if not self.is_empty() else None
    def top(self):
        return self.data[-1] if not self.is_empty() else None
    def is_empty(self):
        return len(self.data) == 0
    def size(self):
        return len(self.data)


def isValid(s):
    if len(s) % 2 != 0:
        return False
    
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = Stack()
    
    for i in s:
        if i in "([{":
            stack.push(i)
        else:
            top = stack.top()
            if top is None or pairs.get(i) != top:
                return False
            stack.pop()
    
    return stack.is_empty()

"""
Bài toán này có thể được giải thích như sau:
- Đối với bài toán ghép cặp thế này, thì đã là cặp thì phải luôn luôn là số chẵn, cho nên phải kiểm tra s, nếu s lẻ --> trả về False ngay lập tức
- Các cặp dấu phải đi với nhau, dấu đóng cặp dấu mở tương ứng. Tạo một dict để lưu trữ dấu và cặp dấu tương ứng, ở đây là dấu đóng là khóa, dấu mở tương ứng là giá trị
- Duyệt chuỗi s bằng biến vòng lặp i, nếu i thuộc các dấu mở -> đẩy vào stack
- Ngược lại, nếu không phải dấu mở, lấy ra phần tử cuối stack (tức là trên đầu), nếu top không tồn tại hoặc dấu đóng gần nhất không cùng cặp với top --> return False ngay lập tức
- Nếu không có vấn đề gì, tuần tự pop phần top của stack rồi tiếp tục kiểm tra, cho đến khi stack rỗng --> thỏa mãn điều kiện đề bài

Phiên bản không dùng stack:
def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        pairs = {')':'(', ']':'[', '}':'{'}
        stack = []

        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack or stack[-1] != pairs[i]:
                    return False
                stack.pop()
        
        return not stack
"""
