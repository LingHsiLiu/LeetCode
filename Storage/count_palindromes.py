## Pure Storage

def count_palindromes(S):
    str_len = len(S)
    result = 0
    for middle in range(str_len*2 - 1):
        head = middle // 2
        tail = head + middle % 2
        while head >= 0 and tail < str_len and S[head] == S[tail]:
            result += 1
            head -= 1
            tail += 1
    return result



# S = "ASANtaLivedAsAdeviLatNASA"
S = "hellolle"
# S = "wowpurerocks"

print(count_palindromes(S))
