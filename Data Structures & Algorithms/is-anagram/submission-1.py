class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenins = {}
        seenint = {}
        for i in s:
            seenins[i] = seenins.get(i, 0) + 1
        for i in t:
            seenint[i] = seenint.get(i, 0) + 1
        if seenins == seenint:
            return True
        return False