class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # all possible subsets, so use backtracking
        # You can traverse this tree as down as possible and just append to the list. Then just simply backtrack.
        # Only recursively call when the condition is met.
        # In the case of permutations, it's only called when the avail array is iterable. Otherwise it doesn't get    called

        # Condition when to append r_type_contents to r_type
        # Only recursively call when the condition is met. The condition for typical "subsets" or "permutations"
        r_type_contents = []
        r_type = []
        avail = nums
        self.helper(avail, r_type, r_type_contents)
        return r_type

        # avail[i+1:] handles the traversal to getting [], [1], [1,2] and [1,2,3].
        # The [2] and [2,3] and [3] get handled from the first for loop where you're appending avail[i]
    def helper(self, avail, r_type, r_type_contents):
        print avail, r_type_contents
        r_type.append(r_type_contents)
        for i in range(len(avail)):
            self.helper(avail[i+1:], r_type, r_type_contents + [avail[i]])
