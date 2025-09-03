
def lengthOfLastWord(s):
    s = " ".join(s.strip().split()).split(' ')
    return len(s[-1])

print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))
print(lengthOfLastWord("Hello World"))
# new_str = " ".join(input_str.split())
