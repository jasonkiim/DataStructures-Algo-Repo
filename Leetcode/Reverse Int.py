class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l1 = [str(i) for i in str(x)]
        l1.reverse()
        result = 0
        if "-" in l1:
            l1.remove("-")
            result = -int("".join(l1))
        else:
            result = int("".join(l1))
        if result > 2**31 or result < -2**31:
            return 0
        return result
