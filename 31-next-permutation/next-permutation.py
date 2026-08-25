class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2
        
        # Step 1: Find pivot
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find successor
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse suffix
        nums[i+1:] = reversed(nums[i+1:])
