class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeString(self, A, B):
        i, j = 0, 0
        C = []
        A = A.split()
        B = B.split()
        while i < len(A) and j < len(B):
            if i <= j:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        while i < len(A):
            C.append(A[i])
            i += 1
        while j < len(B):
            C.append(B[j])
            j += 1
        C = " ".join(C)
        return C


if __name__== "__main__":
    A = "Hello Word Bob ice cream"
    B = "Sister Like John"
    result = Solution().mergeString(A,B)
    print(result)
