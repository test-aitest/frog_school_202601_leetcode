class Solution {
    func moveZeroes(_ nums: inout [Int]) {
        var i = 0
        nums.forEach {
            if ($0 != 0) {
                nums[i] = $0
                i+=1
            }
        }

        for k in i ..< nums.count {
            nums[k] = 0
        }
    }
}