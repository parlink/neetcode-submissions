class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        if len(s) != len(t):
            return False
        for i in s:
            seen[i] = seen.get(i, 0) + 1
        for i in t:
            seen[i] = seen.get(i, 0) - 1
        return all(count == 0 for count in seen.values())