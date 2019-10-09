class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        stone_set = set(stones)
        aleady_used = set()
        stack = [(0,0)]

        while stack:
            stone, jump = stack.pop()
            for i in (jump-1, jump, jump+1):
                s = stone + i
                # Ensure that the next possible step is in the stone_set, jump is always greater than 0, and always not going backwards (accomplished by checking the s, i in aleady_used)
                if i > 0 and s in stone_set and not (s,i) in aleady_used:
                    if s == stones[-1]:
                        return True
                    stack.append((s,i))
            aleady_used.add((stone, jump))

        return False
                
