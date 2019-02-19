class Solution(object):
    def isHappy(self, n):
        timeout = 0
        return self.helper_func(n, timeout)
        """
        :type n: int
        :rtype: bool
        """

    def helper_func(self, n, timeout):
        sum = 0
        for i in str(n):
            sum += int(i) ** 2

        if sum == 1:
            return True
        elif timeout == 5:
            return False
        else:
            return self.helper_func(sum, timeout+1)



# Horrible answer, is not scalable at all.
# When asked in the interview, make sure to ask
# when you can expect the algorithm to "time_out" and return False
