class Solution {
    func validMountainArray(_ arr: [Int]) -> Bool {
        var i = 1
        while (i < arr.count && arr[i-1] < arr[i]) {
            i += 1
        }
        if (i == 1 || i == arr.count) {
            return false
        }
        while (i < arr.count && arr[i] < arr[i-1]) {
            i += 1
        }

        return i == arr.count
    }
}