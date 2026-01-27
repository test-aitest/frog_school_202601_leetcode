class Solution {
    func missingNumber(_ nums: [Int]) -> Int {
        var dictionary = [Int: Bool]()
        var output = 0
        nums.forEach { num in 
            dictionary[num] = true       
        }

        for i in 1 ... nums.count {
            if !(dictionary[i] ?? false) {
                output = i
            }
        }

        return output
    }
}