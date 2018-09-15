def StringLengthK(string, k):
    if k == 0 or not string:
        return []
    hash = {}
    result = []
    start = 0

    for i in range(len(string)):
        if string[i] in hash:
            idx = hash[string[i]]
            for j in range(start, idx):
                hash.pop(string[j])
            start = idx + 1
        else:
            if i - start + 1 > k:
                hash.pop(string[start])
                start += 1
        hash[string[i]] = i
        if i - start + 1 == k:
            result.append(string[start:i+1])
    return result


input = "barfoothefoobarman"
k = 4
print(StringLengthK(input, k))
