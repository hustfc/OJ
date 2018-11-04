class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []: return ''
        str = ''
        flag = 1
        index = 0
        length = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < length:
                index = i
                length = len(strs[i])
        for m in range(len(strs[index])):
            c = strs[index][m]
            for i in range(len(strs)):
                if c != strs[i][m]:
                    flag == 0
                    return str
            if flag == 1:
                str += c
        return str
strs = ['aa', 'a']
print(Solution().longestCommonPrefix(strs))

