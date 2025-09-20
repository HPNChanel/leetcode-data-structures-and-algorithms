
def separateDigits(num: int) -> int:
    sum_digits = 0
    
    while num > 0:
        sum_digits += num % 10
        num //= 10
    
    return sum_digits


def addDigits(num: int) -> int:
    
    rel = num
    
    while len(str(rel)) > 1:
        rel = separateDigits(rel)

    return rel


print(addDigits(38))
print(addDigits(0))
