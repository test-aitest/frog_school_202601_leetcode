# Combination Sum

[![Conbination sum 2]()]()

# Understand Match
## question
- Does candidates contain duplicates interger? Yes
- Are candidates sorted? No
- If candidates are empty, what should we return? - The length of candidates is at least 1.
- If we are impossible to make any combinations, what shoud we return? For example candidates = [2], target = 5. - You should return the empty array.

## happy path
ex.1
candidates = [9,2,2,4,6,1,5], target = 8
res = [[1,2,5],[2,2,4],[2,6]]

ex.2
candidates = [1,2,3,4,5], target = 7
res = [[1,2,4], [2,5], [3,4]]

## edge case
candidates = [2], target = 5
res = []

## constraints
- Just to confirm, do we have any constraints? 
Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

# Plan
Let's look at example 1.
candidates = [9,2,2,4,6,1,5], target = 8
res = [[1,2,5],[2,2,4],[2,6]]
And look at [2, 2, 4] combination.
We can find each element in candidates can be used at most once.
Candidates have duplicates, it's 2. So we can use the number "2" maximum two times in the one combination subarray.
Int the different combination, we can use the same element any time. That's why we can use 2 in the [1,2,5] and [2,2,4].

# Implement
# Review Evaluate

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
```