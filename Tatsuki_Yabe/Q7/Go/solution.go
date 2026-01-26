package main

/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */
func isBadVersion(version int) bool

func firstBadVersion(n int) int {
	var left = 1
	var right = n
	for left < right {
		var mid = (left + right) / 2
		if isBadVersion(mid) {
			return mid
		} else {
			left = mid + 1
		}
	}

	return left
}
