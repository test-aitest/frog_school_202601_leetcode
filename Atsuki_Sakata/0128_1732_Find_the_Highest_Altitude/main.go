package main

func largestAltitude(gain []int) int {
	var nowAltitude, maxAltitude int
	for _, diff := range gain {
		nowAltitude += diff
		if nowAltitude > maxAltitude {
			maxAltitude = nowAltitude
		}
	}
	return maxAltitude
}

/*
## Solution
This problem asks us to find the highest altitude reached during a bike trip.
A biker starts at altitude 0, and we are given an array gain where gain[i] represents the net altitude change between point i and point i*1.

## Approach (Prefix Sum)
We can solve this by computing the running sum of altitude changes while tracking the maximum altitude seen.
- nowAltitude keeps track of the current altitude (cumulative sum of gains).
- maxAltitude keeps track of the highest altitude encountered so far.

## Algorithm
1. Initialize nowAltitude and maxAltitude to 0 (starting altitude is 0).
2. Iterate through the gain array:
  - Add the current gain to nowAltitude to get the altitude at the next point.
  - If nowAltitude exceeds maxAltitude, update maxAltitude.
3. Return maxAltitude as the result.

## Why This Works
The altitude at any point is the prefix sum of all gains up to that point.
By maintaining a running sum and comparing it against the maximum seen so far, we efficiently find the peak altitude in a single pass.
Note that the starting altitude (0) is implicitly considered since maxAltitude is initialized to 0.

## Complexity
### Space Complexity: O(1)
We only use two integer variables regardless of the input size.

### Time Complexity: O(n)
We traverse the gain array once, performing constant-time operations at each step.
*/
