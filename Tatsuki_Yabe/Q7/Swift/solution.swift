/**
 * The knows API is defined in the parent class VersionControl.
 *     func isBadVersion(_ version: Int) -> Bool{}
 */

class Solution : VersionControl {
    func firstBadVersion(_ n: Int) -> Int {
        var left = 1
        var right = n
        while(left < right) {
            var mid = (left + right) / 2
            if (isBadVersion(mid)) {
                return mid
            } else {
                left = mid + 1
            }
        }

        return left
    }
}