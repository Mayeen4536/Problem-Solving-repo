class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            for x in strs:
                if x[i] != ch:
                    return shortest[:i]
        return shortest
