package main

func missingNumber(nums []int) int {
	numMap := make(map[int]bool, len(nums))
	output := 0
	for _, num := range nums {
		numMap[num] = true
	}

	for i := 1; i <= len(nums); i++ {
		if !numMap[i] {
			output = i
		}
	}

	return output
}
