from collections import defaultdict


class Solution:
    def can_spell(self, magazine: list[str], note: str) -> bool:
        letters = defaultdict(int)
        for letter in magazine:
            letters[letter] += 1

        for letter in note:
            if letters[letter] <= 0:
                return False
            letters[letter] -= 1
        return True


if __name__ == "main":
    assert Solution().canSpell(["a", "b", "c", "d", "e", "f"], "bed")

    assert not Solution().canSpell(["a", "b", "c", "d", "e", "f"], "cat")
