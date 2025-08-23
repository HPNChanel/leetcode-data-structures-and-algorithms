
"""
Roman        Integer
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

"""

my_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}

def romanToInt(s: str) -> int:
        my_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}
        
        rel = my_dict[s[-1]]
        for i in range(len(s) - 1):
            if my_dict[s[i]] >= my_dict[s[i + 1]]:
                rel += my_dict[s[i]]
            else:
                rel -= my_dict[s[i]]

        return rel