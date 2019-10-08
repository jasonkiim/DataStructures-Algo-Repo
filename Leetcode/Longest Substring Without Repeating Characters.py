class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {}
        l, r, max_count = 0, 0, 0

        # Append the values to the dictionary. Have 2 pointers, l and r.
        # If the value isn't in the dictionary, append the value in the dictionary and increment r. Then compare the prev max and the current max and set the max, where max is determined by r - l.
        # If the character is in the dictionary, then remove the most left value, and increment left value until the value is no longer in the dictionary.
        # We want to iterate this while l and r are both less than the length of the string.
        # Time:  O(2n) so basically O(n) as dictionary lookup/deletion is O(1)
        # Space: O(k), where k is the length of the longest substring w/o repeating characters

        while l < len(s) and r < len(s):
            print s[r]
            if not s[r] in dic:
                dic[s[r]] = 1
                r += 1
                max_count = max(max_count, r-l)
            else:
                del dic[s[l]]
                l += 1
        return max_count
