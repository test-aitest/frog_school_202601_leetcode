# Permutations
# Understand Match
First let me clarify the problem.
- array of distinct intergers

## question
- How many intergers do nums contain at most and at least? -> 1 <= nums.length <= 6
- How range of nums[i] ? -> -10 <= nums[i] <= 10

## happy path
nums = [1, 2, 3], permutations = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

## edge case
nums = [1], permutations = [[1]]

## constraints
We already know because we asked some questions.

# Plan
- Backtracking
- Recursive + subproblem approach(recommended by Neet code)

# Implement
```python
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        # Base case: if input is empty, return a list containing an empty list
        if len(nums) == 0:
            # We don't need this base case because at least nums length is 1.
            # But this approach decrease elements of nums. So finally, length of nums reach 0.
            # This is guard clause for that.
            return [[]] 
            
        # Recursive step
        # Get all permutations of the subarray excluding the first element
        perms = self.permute(nums[1:])
        res = []
        
        # Take the first element and insert it into every possible position
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p[:] # Create a copy
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        return res    
```

# Review Evaluate
