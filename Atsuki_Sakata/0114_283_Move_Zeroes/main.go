package main

func moveZeroes(nums []int) {
	var count int
	for i := range nums {
		if nums[i] == 0 {
			count++
		} else {
			nums[i-count] = nums[i]
		}
	}

	for i := 0; i < count; i++ {
		nums[len(nums)-1-i] = 0
	}
}

/*
## Solution
This problem is an array transformation task.
We are asked to move all zeros to the end of the array while preserving the relative order of non-zero elements.

Instead of using an extra array, we can do this in-place by compacting all non-zero elements to the front and then filling the rest with zeros.

## Approach (Two Pointers with Shift Count)
We iterate through the array once and keep track of how many zeros we have seen so far.
- i works as the first pointer scanning the array.
- count represents how many zeros have appeared before index i.
- For each non-zero element, we shift it left by count positions.

This effectively packs all non-zero elements to the front while keeping their original order.

After that, we fill the last count positions with zeros.

## Algorithm
1. Initialize count is 0 to track how many zeros have been seen.
2. Traverse the array from left to right:
  - If noms[i] is zero, increment count.
  - Otherwise, move the element to nums[i - count].
3. After the traversal, fill the last count elements of the array with zeros.

## Why This Works
At any point during traversal:
- All elements before index i - count are already valid non-zero elements in correct order.
- count tells us exactly how far left the current non-zero element should be shifted.

So we never lose unprocessed data, and we maintain stability (relative order).

## Complexity Analysis
### Space Complexity: O(1)
The transformation is done in-place with constant extra space.

### Time Complexity: O(n)
One pass to shift non-zero elements and one pass to fill zeros -> O(2n) -> simplified to O(n).

This solution is space-optimal, though it may still perform unnecessary writes when many elements are already in correct positions.
An even more optimal variant would reduce the number of writes by swapping only when needed.
*/
