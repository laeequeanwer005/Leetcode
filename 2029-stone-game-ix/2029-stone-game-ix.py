class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:

        count0 = 0
        count1 = 0
        count2 = 0

        # Count remainders
        for stone in stones:
            if stone % 3 == 0:
                count0 += 1
            elif stone % 3 == 1:
                count1 += 1
            else:
                count2 += 1

        # If number of remainder-0 stones is even
        if count0 % 2 == 0:
            return count1 > 0 and count2 > 0

        # If number of remainder-0 stones is odd
        return abs(count1 - count2) > 2