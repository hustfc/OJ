class Solution(object):
    def myMatch(self, s, p, s_index, p_index):
        print(s_index, p_index)
        if p == '' and s != '':
            #print(1)
            return False
        if s == '':
            if p == '' or (len(p) >=2 and p[1] == '*'):
                return True
            else:
                print(2)
                return False
        if p_index == -1:
            if s_index == -1:
                return True
            else:
                print(3)
                return False
        if s_index == -1:
            if p_index == 0:
                if s[0] != p[0]:
                    print(4)
                    return False
                # elif s[0] == p[0]:
                #     return True
            else:
                return self.myMatch(s, p, s_index, p_index - 2)
        if p[p_index] == '*':
            if s_index > -1 and (p[p_index - 1] == '.' or (s[s_index] == p[p_index - 1] and s[s_index - 1] != p[p_index - 2] and p[p_index - 2] != '*')):
                return self.myMatch(s, p, s_index - 1, p_index)
            else:
                return self.myMatch(s, p, s_index, p_index - 2)
        else:
            if p[p_index] == '.' or p[p_index] == s[s_index]:
                return self.myMatch(s, p, s_index - 1, p_index - 1)
            else:
                print(5)
                return False


    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.myMatch(s, p, len(s) - 1, len(p) - 1)

sol = Solution()
print(sol.isMatch('aaa', 'ab*a*c*a'))