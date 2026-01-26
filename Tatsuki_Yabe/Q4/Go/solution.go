package main

func moveZeroes(nums []int) {
	left := 0
	for _, v := range nums {
		if v != 0 {
			nums[left] = v
			left += 1
		}
	}
	for k := left; k < len(nums); k++ {
		nums[k] = 0
	}
}
