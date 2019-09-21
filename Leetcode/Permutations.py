class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # How to divide up the avaiable list to choose from to sets of distinct lists that's one length less than the
        # previous
        # Ex. [1,2,3] into [2,3] [1,3] and [1,2]
        # permuted_ans will simply just be appending the previous + the avail[i]
        # Use a for loop and the index as the core component
        # Base condition is when level of the tree is equal to the length of permuted_ans

        N = len(nums)
        r_type = []
        avail = nums
        permuted_ans = []
        level = 0
        self.helper(avail, permuted_ans, level, r_type, N)
        return r_type

    def helper(self, avail, permuted_ans, level, r_type, N):
        if level == N:
            r_type.append(permuted_ans)
        else:
            for i in range(len(avail)):
                self.helper(avail[:i] + avail[i+1:], permuted_ans+[avail[i]], level+1, r_type, N)


    
