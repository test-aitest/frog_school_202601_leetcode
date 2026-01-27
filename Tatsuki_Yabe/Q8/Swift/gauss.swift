class Solution {
    func missingNumber(_ nums: [Int]) -> Int {
        var len = nums.count
        var intendedSum = len * (len + 1) / 2
        var actualSum = 0

        for num in nums {
            actualSum += num
        }

        return intendedSum - actualSum
    }
}