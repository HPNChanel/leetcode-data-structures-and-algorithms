
def mySqrt(x: int) -> int:
    if x < 2:
        return x
    
    y = x
    while True:
        y_next = (y + x // y) // 2
        if y_next >= y:
            return y if y * y <= x else y - 1
        y = y_next
