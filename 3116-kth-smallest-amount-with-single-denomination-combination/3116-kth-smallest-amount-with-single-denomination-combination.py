#Using Inclusion-Exclusion + LCM
from math import gcd
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            n = len(coins)

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):

                current_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        current_lcm = lcm(current_lcm, coins[i])

                amount = x // current_lcm

                if bits % 2 == 1:
                    total += amount
                else:
                    total -= amount

            return total

        left = 1
        right = max(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
