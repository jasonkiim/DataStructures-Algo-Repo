class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dic = {}
        i = 0
        for i in range(len(s)):
            if s[i] in s_dic:
                s_dic[s[i]] += 1
            else:
                s_dic[s[i]] = 1

        for j in range(len(t)):
            if t[j] in s_dic:
                s_dic[t[j]] -= 1
            else:
                return False

        return all(v == 0 for v in s_dic.values())
