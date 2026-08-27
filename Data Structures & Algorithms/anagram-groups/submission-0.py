class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch)-ord('a')] += 1
            key = tuple(count)
            mp.setdefault(key, []).append(s)
        return list(mp.values())