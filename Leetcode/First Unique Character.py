class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {}

        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        # Because we can't maintain the order in the dictionary, iterate through the string once again...
        for c in s:
            if dic[c] == 1:
                return s.find(c)
        return -1
