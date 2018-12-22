# 53. Reverse Words in a String
# Given an input string, reverse the string word by word.

# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        # print(s)
        # s = s.split(" ")
        # print(s)
        # return " ".join(s.split(" ")[::-1])
        # return " ".join(s.split(" ")[::-1])
        # return ' '.join(reversed(s.strip().split())) ## miss space
        return ' '.join((s.strip().split())[::-1]) ## miss space
