# 685. First Unique Number In Stream
# Given a continuous stream of numbers, write a function that returns the first unique number whenever terminating number is reached(include terminating number). If there no unique number before terminating number or you can't find this terminating number, return -1.

# Example
# Given a stream [1, 2, 2, 1, 3, 4, 4, 5, 6] and a number 5
# return 3

# Given a stream [1, 2, 2, 1, 3, 4, 4, 5, 6] and a number 7
# return -1


class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        if not nums:
            return -1
        dic = {}
        ans = None
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
            if n == number:
                break
        
        for k, v in dic.items():
            if dic[k] == 1:
                ans = k
                break
        if ans is None or number not in dic:
            return -1
        return ans
                        
