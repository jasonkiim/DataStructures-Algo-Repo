class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Sort the list of nums first
        # Use i as the starting index, and use l and r index pointers to determine whether the sum = 0!
        # Need to handle the duplicacy for all 3 indexes, i, l, and r
        # Handle i duplicacy by checking if nums[i] == nums[i-1] and i > 0
        # Handle l and r duplicacy by first moving to the index containing the last duplicating element,
        # then increment l and decrement r to get to different set of unique elements!

        nums.sort()
        r_type = []

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums)-1
            while l < r:
                print l, r
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    r_type.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return r_type
