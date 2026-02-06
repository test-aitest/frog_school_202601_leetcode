package main

func findDifference(nums1 []int, nums2 []int) [][]int {
	set1 := make(map[int]struct{}, len(nums1))
	set2 := make(map[int]struct{}, len(nums2))

	for _, x := range nums1 {
		set1[x] = struct{}{}
	}
	for _, x := range nums2 {
		set2[x] = struct{}{}
	}

	out1 := make([]int, 0)
	for x := range set1 {
		if _, ok := set2[x]; !ok {
			out1 = append(out1, x)
		}
	}

	out2 := make([]int, 0)
	for x := range set2 {
		if _, ok := set1[x]; !ok {
			out2 = append(out2, x)
		}
	}

	return [][]int{out1, out2}
}

/*
## Solution
We solve this problem by using hash sets to efficiently track the unique elements in each array and compute the difference between them.
By converting both input arrays into sets, we can easily identify which elements appear in one array but not the other.

## Approach (Set/HashMap)
We use hash sets to efficiently compare the elements of the two arrays.
By converting each array into a set, we automatically remove duplicated and enable constant-time lookups.
Then, we iterate over each set and collect the elements that do not appear in the other set.
This allows us to find all distinct values that exist in one array but not in the other in a clean and efficient way.

## Algorithm
1. Convert nums1 into a hash set set1 to remove duplicates.
2. Convert nums2 into a hash set set2 to remove duplicates.
3. Initialize an empty list out1.
4. For each element in set1, if it does not exist in set2, add it to out1.
5. Initialize an empty list out2.
6. For each element in set2, if it does not exist in set1, add it to out2.
7. Return [out1, out2].

## Why This Works
Hash sets provide O(1) average-time membership checks.
By deduplicating the input arrays first, we ensure that each element is processed only once.
This guarantees that the output lists contain only distinct values and that we efficiently find elements that are unique to each array.

## Complexity
### Space Complexity: O(n + m)
We store the distinct elements of nums1 and nums2 in two hash sets.

### Time Complexity: O(n + m)
Each element of nums1 and nums2 is processed once when building the sets, and each distinct element is checked once when computing the differences.
*/
