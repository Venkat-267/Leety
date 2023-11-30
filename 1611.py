class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        flag = 0
        for i in range(31, -1, -1):
            if ((n >> i) & 1) == 1:
                if flag == 0:
                    ans = ans + ((1 << (i + 1))) - 1
                    flag = 1
                else:
                    ans = ans - ((1 << (i + 1)) - 1)
                    flag = 0
        return ans

