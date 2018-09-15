######## reorder log file (2.)
def reorderLines(logFileSize, logLines):
    from functools import cmp_to_key
    def mySort(s1, s2):
        idx1 = s1.find(' ')
        idx2 = s2.find(' ')
        prefix1 = s1[:idx1]
        prefix2 = s2[:idx2]
        log1 = ''.join(s1[idx1 + 1:].split(' ')).lower()
        log2 = ''.join(s2[idx2 + 1:].split(' ')).lower()
        if log1 == log2:
            # tmp1, tmp2 = 0, 0
            # if prefix1 == prefix2: return -1
            # while tmp1 < idx1 or tmp2 < idx2:
            #     if tmp1 == idx1: return -1
            #     if tmp2 == idx2: return 1
            #     if ord(prefix1[tmp1]) < ord(prefix2[tmp2]): return -1
            #     if ord(prefix1[tmp1]) > ord(prefix2[tmp2]): return 1
            #     tmp1 += 1
            #     tmp2 += 1
            if prefix1 < prefix2: return -1
            return 1
        elif log1 < log2:
            return -1
        return 1

    if logFileSize == 0: return logLines
    ret = [''] * logFileSize
    alphaLines = []
    idx = logFileSize - 1
    for i in reversed(range(logFileSize)):
        start = logLines[i].find(' ') + 1
        if logLines[i][start].isdigit():
            ret[idx] = logLines[i]
            idx -= 1
        else:
            alphaLines.append(logLines[i])

    alphaLines.sort(key=cmp_to_key(mySort))
    for i in range(len(alphaLines)):
        ret[i] = alphaLines[i]
    return ret


logFileSize = 5
a = ["a1 9 2 3 1", "a1c Act car", "zo4 4 7", "ab1 off KEY dog", "a1b act car"]
b = ["mi2 jog mid pet", "wz3 34 54 398", "a1 alps cow bar", "x4 45 21 7"]
c = ["t2 13 121 98", "r1 box ape bit", "b4 xi me nu", "br8 eat nim did", "w1 has uni gry", "f3 52 54 31"]
print(reorderLines(logFileSize, a))
