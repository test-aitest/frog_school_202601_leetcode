package main

func maxArea1(height []int) int {
	max_area := 0
	n := len(height)
	for p1 := range n {
		for p2 := p1 + 1; p2 < n; p2++ {
			length := min(height[p1], height[p2])
			width := p2 - p1
			area := length * width
			max_area = max(max_area, area)
		}
	}

	return max_area
}
