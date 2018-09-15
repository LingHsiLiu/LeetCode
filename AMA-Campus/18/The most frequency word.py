##九章

class Solution:
    """
    @param s: a string
    @param excludewords: a dict
    @return: the most frequent word
    """
    def frequentWord(self, s, excludewords):
        # Write your code here
        map = {}
        
        while len(s) > 0:
            end = s.find(' ') if s.find(' ') > -1 else len(s)
            word = s[:end] if s[end-1].isalpha() else s[:end-1]
            s = s[end+1:]
            if word not in excludewords:
                if word in map:
                    map[word] += 1 
                else:
                    map[word] = 1

        max = -1
        res = []
        for key, val in map.items():
            if val == max:
                res.append(key)
            elif val > max:
                max = val
                res = [key]
                
        res.sort()
        
        return res[0]
