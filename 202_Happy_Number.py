
def next_val(n: int) -> int:
    s = 0
    while n:
        n, d = divmod(n, 10)
        s += d * d
    return s


def isHappy(n: int) -> int:
    slow = n
    fast = n
    while True:
        slow = next_val(slow)  #* 1 step
        fast = next_val(next_val(fast))  #* 2 steps
        if slow == 1 or fast == 1:  #* Meet the target 1
            return True
        if slow == fast:  #* Meet in cycle !=1
            return False

print(isHappy(19))
print(isHappy(2))
