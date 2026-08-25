class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        short = min(strs)
        long = max(strs)
        for idx, ch in enumerate(short):
            if ch == long[idx]:
                ans += ch
            else:
                return ans
        return ans