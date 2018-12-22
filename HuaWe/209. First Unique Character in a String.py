# 209. First Unique Character in a String
# Find the first unique character in a given string. You can assume that there is at least one unique character in the string.

# Example
# For "abaccdeff", return 'b'.

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        counter = {}
        
        for c in str:
            counter[c] = counter.get(c, 0) + 1 # 0 是default 如果沒有值
            # print(counter)
        
        for c in str:
            if counter[c] == 1:
                return c
