def        # I could just place each number into a dictionary with an incremental index. Then I'll have a custom loop counter where it resets at len(nums) -1 back to 0. So based on the value that you give, you start the loop+k, and break when the new list is the same size as the original's and simply just return the new list at the end :)

        # dic = {}
        # temp = 0
#         for i, v in enumerate(nums):
#             dic[i] = v


#         for i in range(0, len(nums)-1):
#             i = i+k
#             if i == len(nums)-1:
#                 i = 0

#             if


        # No this is a stupid idea, there must be a better way.

#         temp = 0


#         for i in range(0, len(nums)-1):
#             if i == len(nums)-1:
#                 i = 0

#             if temp == k:
#                 break;

#             nums[i] = nums[i+1]
#             print nums[i]
#             temp += 1
#             print nums

class Solution(object):
    '''
    [1,2,3,4,5,6,7,8,9,10] k = 4
    []
    '''
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        nums1 = []
        nums2 = []

        k = k % len(nums)

        nums1 = nums[len(nums)-k:]
        nums2 = nums[:len(nums)-k]
        print nums1
        print nums2

        nums[:] = nums[len(nums)-k:] +nums[:len(nums)-k]
    # The key to this question is understanding that when you reach the end of the list, you can reset the index.
    # This accomplished as follows: k = k % len(nums), this means that k will be 0 when k = len(nums)


    # Also another key thing to note is that you can directly change the reference of the array via nums[:] if we want to use array = x + y

    
