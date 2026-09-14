from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            result.append(current[:])  # store current subset

            for i in range(start, len(nums)):
                current.append(nums[i])      # choose
                backtrack(i + 1, current)    # explore
                current.pop()                # unchoose

        backtrack(0, [])
        return result