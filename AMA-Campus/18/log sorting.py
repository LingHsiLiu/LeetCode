## python2

class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def cmpFunction(self, a, b):
        idxA = a.find(" ")
        titleA = a[:idxA]
        conA = a[idxA + 1:]
        idxB = b.find(" ")
        titleB = b[:idxB]
        conB = b[idxB + 1:]
        if conA != conB:
            if conA < conB:
                return -1
            else:
                return 1    
        if titleA < titleB:
            return -1
        else:
            return 1
        
    def logSort(self, logs):
        # Write your code here
        res = sorted(logs, cmp=self.cmpFunction)
        ans = []
        for log in res:
            idx = log.find(" ")
            if log[idx + 1].isalpha():
                ans.append(log)
        for log in logs:
            idx = log.find(" ")
            if not log[idx + 1].isalpha():
                ans.append(log)
        return ans
