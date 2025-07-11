class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cmnpreffix = strs[0]

        for x in strs:
            while not x.startswith(cmnpreffix):
                cmnpreffix = cmnpreffix[:-1]
                if not cmnpreffix:
                    return ""

        return cmnpreffix