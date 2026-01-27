package main

func missingNumber2(nums []int) int {
	len := len(nums)
	intendedSum := len * (len + 1) / 2
	actualSum := 0

	for _, num := range nums {
		actualSum += num
	}

	return intendedSum - actualSum
}
