class Solution(object):
# The trick to this question is that you're storing the values from nums as the key of the dictionary 'storage'
# Then when you do a lookup to see if the key exists in the storage dictionary, then return the value of the dictionary which is the index, and i
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        storage = {}
        for i in range(len(nums)):
            if target-nums[i] in storage:
                return [storage[target-nums[i]], i]
            else:
                storage[nums[i]] = i
