class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while c or a or b:
            if c % 2 == 0:
                ans += a % 2 + b % 2
            elif a % 2 == 0 and b % 2 == 0:
                ans += 1
            c //= 2
            a //= 2
            b //= 2
        return ans