package main

func pivotIndex(nums []int) int {
	var sum int
	for _, num := range nums {
		sum += num
	}

	leftSum := 0
	rightSum := sum
	for i := range nums {
		if i != 0 {
			leftSum += nums[i-1]
		}
		rightSum -= nums[i]

		if leftSum == rightSum {
			return i
		}
	}
	return -1
}

/*
## Solution
This problem asks us to find the pivot index of an array.
The pivot index is where the sum of all elements strictly to the left equals the sum of all elements strictly to the right.
If no such index exists, return -1.

## Approach (Prefix Sum)
We can solve this by first computing the total sum, then iterating through the array while maintaining left and right sums.
- leftSum keeps track of the sum of elements to the left of the current index.
- rightSum keeps track of the sum of elements to the right of the current index.

## Algorithm
1. Calculate the total sum of the array.
2. Initialize leftSum to 0 and rightSum to the total sum.
3. Iterate through each index i:
  - If i > 0, add num[i-1] to leftSum (element that is now to the left).
  - Subtract num[i] from rightSum (current element is not part of the right side).
  - If leftSum equals rightSum, return i as the pivot index.
4. If no pivot index is found, return -1.

## Why This Works
At any index i, leftSum represents the sum of elements from index 0 to i-1, and rightSum represents the sum of elements from index i+1 to the end.
By updating these values incrementally as we move through the array, we avoid recalculating sums from scratch.
The first index where leftSum equals rightSum is our pivot index.

## Complexity
### Space Complexity: O(1)
We only use a constant number of variables (sum, leftSum, rightSum) regardless of input size.

### Time Complexity: O(n)
We traverse the array twice: once to calculate the total sum, and once to find the pivot index.
*/
