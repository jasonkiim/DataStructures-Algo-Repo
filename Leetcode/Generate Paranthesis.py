class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # all combinations aka backtracking
        # You can only put a right paren when the value of right parens left is
        # greater than left parens left

        left_paren_left = n
        right_paren_left = n
        rType = []
        rContents = ""

        self.helper(rType, rContents, left_paren_left, right_paren_left)
        return rType

    def helper(self, rType, rContents, left_paren_left, right_paren_left):
        # Base case is when all the parenthesis are used
        if left_paren_left == 0 and right_paren_left == 0:
            rType.append(rContents)
        else:
            # The first case to check is when left_paren_left exists
            if left_paren_left > 0:
                self.helper(rType, rContents + "(", left_paren_left-1, right_paren_left)
            # If there's more right parens to be put than left parenthesis, then
            # plcae the right parenthesis.
            if left_paren_left < right_paren_left:
                self.helper(rType, rContents + ")", right_paren_left, right_paren_left-1)
    
