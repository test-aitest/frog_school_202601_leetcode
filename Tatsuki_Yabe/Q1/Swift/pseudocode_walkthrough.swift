class Solution {
    func maxArea2(_ height: [Int]) -> Int {
        var l = 0
        var r = height.count - 1
        var maxarea = 0

        while l < r {
            let length = min(height[l], height[r])
            let width = r - l
            let area = length * width
            maxarea = max(maxarea, area)

            if (l < r) {
                l += 1
            } else {
                r -= 1
            }
        }


        return maxarea
    }
}