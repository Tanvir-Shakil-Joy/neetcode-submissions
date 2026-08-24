class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        maps, mapt = {}, {}
        for idx in range(len(s)):
            maps[s[idx]] = 1+maps.get(s[idx], 0)
            mapt[t[idx]] = 1+mapt.get(t[idx], 0)
        for ch in s:
            if maps[ch] != mapt.get(ch, 0):
                return False
        return True