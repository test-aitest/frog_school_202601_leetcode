class Solution {
    func maxArea1(_ height: [Int]) -> Int {
        var maxarea = 0
        var n = height.count

        for p1 in 0..<n {
            for p2 in p1+1..<n{
                let lenght = min(height[p1], height[p2])
                let width = p2 - p1
                let area = lenght * width
                maxarea = max(maxarea, area)
            }
        }

        return maxarea
    }
}