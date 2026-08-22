class Solution:
    def permute(self, nums):
        result = []
        
        def backtrack(path, remaining):
            if not remaining:
                result.append(path[:])  # add a copy of path
                return
            for i in range(len(remaining)):
                # choose
                path.append(remaining[i])
                # explore
                backtrack(path, remaining[:i] + remaining[i+1:])
                # un-choose
                path.pop()
        
        backtrack([], nums)
        return result
