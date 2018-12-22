# 960. First Unique Number in a Stream II
# We need to implement a data structure named DataStream. There are two methods required to be implemented:

# void add(number) // add a new number
# int firstUnique() // return first unique number
# Example
# add(1)
# add(2)
# firstUnique() => 1
# add(1)
# firstUnique() => 2

class DataStream:

    def __init__():
        # do intialization if necessary

        self.mapping = {}
        self.queue = []
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        self.queue.append(num)
        if num in self.mapping:
            self.mapping[num] = self.mapping[num] +1 
        else:
            self.mapping[num] = 1 
    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        while len(self.queue) > 0 and self.mapping[self.queue[0]] > 1:
            self.queue.pop(0)

        if len(self.queue) == 0:
            return -1
        else:
            return self.queue[0]
