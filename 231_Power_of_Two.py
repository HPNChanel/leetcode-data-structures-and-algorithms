
from math import sqrt, ceil

def isPowerOfTwo(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


"""
Quy tắc:
n & (n - 1) xóa bit 1 thấp nhất. Nếu kết quả là 0 thì n có đúng một bit 1
n > 0 để loại ra 0 và số âm 

"""
