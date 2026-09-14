from collections import Counter, defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, word: List[str]) -> List[int]:
        need = Counter(word)

        word_len = len(word[0])
        word_cnt = len(word)
        n = len(s)

        res = []

        for offset in range(word_len):
            left = offset
            have = defaultdict(int)
            cnt = 0

            for i in range(left, n - word_len + 1, word_len):
                curr = s[i:i + word_len]

                # Current word cannot be part of a valid window
                if curr not in need:
                    have.clear()
                    cnt = 0
                    left = i + word_len
                    continue

                # Remove words until curr can be added
                while need[curr] < have[curr] + 1:
                    left_word = s[left:left + word_len]
                    have[left_word] -= 1
                    cnt -= 1
                    left += word_len

                have[curr] += 1
                cnt += 1

                if cnt == word_cnt:
                    res.append(left)

                    # Remove the first word and continue looking
                    left_word = s[left:left + word_len]
                    have[left_word] -= 1
                    cnt -= 1
                    left += word_len

        return res