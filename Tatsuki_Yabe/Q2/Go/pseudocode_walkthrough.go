package main

func validMountainArray(arr []int) bool {
	i := 1
	for i < len(arr) && arr[i-1] < arr[i] {
		i++
	}
	for i == 1 || i == len(arr) {
		return false
	}
	for i < len(arr) && arr[i] < arr[i-1] {
		i++
	}

	return i == len(arr)
}
