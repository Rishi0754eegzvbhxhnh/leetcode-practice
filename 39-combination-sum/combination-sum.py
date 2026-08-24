class Solution:
    def combinationSum(self, candidates, target):
        res = []
        
        def backtrack(start, path, target):
            if target == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                path.append(candidates[i])
                backtrack(i, path, target - candidates[i])  # reuse allowed
                path.pop()
        
        backtrack(0, [], target)
        return res
