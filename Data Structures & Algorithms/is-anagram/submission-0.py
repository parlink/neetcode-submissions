class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenins = {}
        seenint = {}
        for i in s:
            if i not in seenins:
                seenins[i]= 0
            if i in s:
                seenins[i] += 1
        for i in t:
            if i not in seenint:
                seenint[i] = 0
            if i in seenint:
                seenint[i] +=1
        if seenins == seenint:
            return True
        return False