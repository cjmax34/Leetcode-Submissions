class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        len_first = len(strs[0])

        for i in range(len_first):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix