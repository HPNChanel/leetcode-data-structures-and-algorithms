
def isPalindrome(s: str) -> bool:
        if len(s) == 1:
            return True
        new_str = [i.lower() for i in s if i.isalnum()]

        if new_str == new_str[::-1]:
            return True
        else:
            return False