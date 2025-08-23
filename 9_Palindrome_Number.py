
def isPalindrome(x: int) -> bool:
        str_n = str(x)
        if str_n == str_n[::-1]:
            return True
        else:
            return False