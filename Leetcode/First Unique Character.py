class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {}

        # Get a count of each characters from the string
        for i in range (0, len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1

        # Iterate through the string once again and get the
        # first character with the counter 1
        for i in range (0, len(s)):
            if dic[s[i]] is 1:
                return s.index(s[i])
        return -1




        
