class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:

        def matches(a, b):
            count = 0

            for i in range(6):
                if a[i] == b[i]:
                    count += 1

            return count

        candidates = words[:]

        for _ in range(30):

            best_word = candidates[0]
            best_score = float("inf")

            for guess in words:

                groups = [0] * 7

                for candidate in candidates:
                    score = matches(guess, candidate)
                    groups[score] += 1

                worst_group = max(groups)

                if worst_group < best_score:
                    best_score = worst_group
                    best_word = guess

                elif worst_group == best_score and guess in candidates:
                    best_word = guess

            result = master.guess(best_word)

            if result == 6:
                return

            candidates = [
                word for word in candidates
                if matches(best_word, word) == result
            ]