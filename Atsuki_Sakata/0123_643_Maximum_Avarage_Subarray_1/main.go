package main

func findMaxAverage(nums []int, k int) float64 {
	numLen := len(nums)
	var sum, maxSum int
	for i := 0; i <= numLen-k; i++ {
		if i == 0 {
			for j := 0; j < k; j++ {
				sum += nums[i+j]
				maxSum = sum
			}
			continue
		}

		sum -= nums[i-1]
		sum += nums[i+k-1]
		if sum > maxSum {
			maxSum = sum
		}
	}
	return float64(maxSum) / float64(k)
}

/*
## Solution
This problem asks me to find the maximum average value of any contigous subarray of length k.
We need to return the maximum average as a floating-point number.

## Approach (Sliding Window)
Instead of recalculating the sum for each window from scratch, we use the sliding window technique.
- Fiest, calculate the sum of the initial window (first k elements).
- Then, slide the window by removing the leftmost element and adding the next element.
- Track the maximum sum encountered.

## Algorithm
1. Initialize sum and maxSum to 0.
2. For the first window (i = 0), calculate the sum of the first k elements.
3. For subsequent windows:
  - Subtract the element leaving the window (nums[i-i]).
  - Add the element entering the window (nums[i+k-1]).
  - Update maxSum if the current sum is greater.
4. Return maxSum divided by k as a float64.

## Why This Works
The sliding window technique avoids redundant calculations.
Each window shares k-1 elements with the previous window, so we only need to adjust for the one element that changes.
This reduces the time complexity from O(n*k) to O(n).

## Complexity Analysis
### Space Complexity: O(1)
We only use a constant number of variables regardless of input size.

### Time Complexity: O(n)
We traverse the array once, performing constant-time operations at each step.
*/
