
from collections import Counter

def canBeTypedWords(text: str, brokenLetters: str) -> int:
    
    broken = set(brokenLetters)
    count = 0
    
    for word in text.split():
        if not (set(word) & broken):  #* Ký tự trong broken KHÔNG giao với tập ký tự trong từ thì count += 1, điều này thỏa mãn việc tránh bị chồng lặp
            count += 1
    
    return count
    


print(canBeTypedWords("hello world", "ad"))
print(canBeTypedWords("leet code", "lt"))
print(canBeTypedWords("leet code", "e"))



